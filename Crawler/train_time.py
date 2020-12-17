import requests
from bs4 import BeautifulSoup
import time

url = 'https://www.railway.gov.tw/tra-tip-web/tip'
staDic = {}
today = time.strftime('%Y/%m/%d')
sTime = '06:00'
eTime = '23:59'


def getTrip(fromStat,toStat):
    resp = requests.get(url)
    if resp.status_code != 200:
        print('網址錯誤'+url)
        return

    soup = BeautifulSoup(resp.text, 'html5lib')
    #找車站
    # stations = soup.find(id ='cityHot').ul.find_all('li')
    # print(stations)
    # print("=======================")
    stations = soup.find_all('button','btn tipStation')
    # print(stations)

    for station in stations:
        stationName = station.text
        stationId = station['title']
        staDic[stationName] = stationId
    #
    #
    csrf = soup.find(id='queryForm').find('input',{'name':'_csrf'})['value']
    formData = {
        'trainTypeList': 'ALL',
        'transfer': 'ONE',
        'startStation': staDic[fromStat],
        'endStation': staDic[toStat],
        'rideDate': today,
        'csrfmiddlewaretoken':csrf,
        'startTime': sTime,
        'endTime': eTime,
        }
    queryUrl = soup.find(id='queryForm')['action']
    qResp = requests.post('https://www.railway.gov.tw'+queryUrl,data=formData)
    qSoup = BeautifulSoup(qResp.text,'html5lib')
    trs = qSoup.find_all('tr','trip-column')
    for tr in trs:
        td = tr.find_all('td')
        print(f'{td[0].ul.li.a.text}|{td[1].text}|{td[2].text}|{td[3].text}|{td[6].text.strip()}')

getTrip('沙鹿','臺中')