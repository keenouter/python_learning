# -*- coding: utf-8 -*-
# @Time    : 2020/7/5 0:28
# @Author  : G.M
# @FileName: remote_ocr.py
# @Software: PyCharm

import requests

url = 'http://127.0.0.1:5000/ocr'
image = {'image': open('Snipaste_2020-07-04_22-54-15.png', 'rb')}
response = requests.post(url, files=image)
print(response.text)
