import logging
import json
import os

import requests
# url = "https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/O-A0084-003?Authorization=rdec-key-123-45678-011121314&downloadType=WEB&format=JSON"
#url ="https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/O-A0084-002?Authorization=rdec-key-123-45678-011121314&downloadType=WEB&format=JSON"
url = 'https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/O-A0084-001?Authorization=rdec-key-123-45678-011121314&downloadType=WEB&format=JSON'
r = requests.get(url)
FORMAT = '%(asctime)s %(levelname)s: %(message)s'
logging.basicConfig(format=FORMAT,level=logging.INFO)
jsons = json.loads(r.text)
print(jsons)
cwbopendata = jsons['cwbopendata']
dataset=cwbopendata['dataset']
url = dataset['resource']['uri']
r.close()
r = requests.get(url)
file = url.strip("https://opendata.cwb.gov.tw/fileapi/opendata/MSC/")+".png"
logging.info(file)
path = "..\\data\\"+file
# if r.status_code == 200:
#     file = open("1.png", "wb")
#     file.write(r.content)
#     file.close()
if r.status_code == 200 :
    with open(path,"wb") as f:
        for chunk in r:
            f.write(chunk)
        f.close()
print("ok")
