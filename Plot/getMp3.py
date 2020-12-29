import logging
import json
import os

import requests
from bs4 import BeautifulSoup

FORMAT = '%(asctime)s %(levelname)s: %(message)s'
logging.basicConfig(format=FORMAT,level=logging.INFO)


# url = 'http://www.family977.com.tw/index.php?route=choice/unit_detail&choice_program_id=17&page=1'

def getmp3(url):

    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html5lib')
    mp3s = soup.find_all('a','play ready')
    mp3urls = []
    for mp3 in mp3s:
        mp3urls.append(mp3['data-ready-href'])
    # urls =  "http://www.family977.com.tw//song/websound/映興電子-好好談心-蘇絢慧10滋養身心篇.mp3"
    for urls in mp3urls:
        r = requests.get(urls)
        file = urls.strip("http://www.family977.com.tw//song/websound/")
        logging.info(file)
        path = "..\\data\\"+file
        if r.status_code == 200 :
            with open(path,"wb") as f:
                for chunk in r:
                    f.write(chunk)
                f.close()
    print(f"page {i} ok")


for i in range(1,10):
    getmp3(url = "http://www.family977.com.tw/index.php?route=choice/unit_detail&choice_program_id=17&page="+str(i))