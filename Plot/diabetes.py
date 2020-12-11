import logging
import json
import os
import requests
url = 'https://quality.data.gov.tw/dq_download_csv.php?nid=9337&md5_url=c60ec418c5b01e8bdf8f1c089384bb0e'

r = requests.get(url)
FORMAT = '%(asctime)s %(levelname)s: %(message)s'
logging.basicConfig(format=FORMAT,level=logging.INFO)
logging.info(r.text)