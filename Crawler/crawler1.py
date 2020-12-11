import requests
from bs4 import BeautifulSoup
#Response 200
resp = requests.get('https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip112/gobytime')
#html
# resp = requests.get('https://code-gym.github.io/spider_demo/')

soup = BeautifulSoup(resp.text,'html5lib')
#利用beautiful 的find方法
print(soup.find('button').text)
divs = soup.find('div')
uls = []
# print(soup)
# for tag in soup.find_all("li"):
#     print(tag.text)


stations = []
#利用class 取得網頁資料
for station in soup.find_all('button','btn tipCity'):
    stations.append(station.text)

print(stations)