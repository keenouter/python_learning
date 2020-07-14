'''
@Author: your name
@Date: 2020-07-04 18:47:44
@LastEditTime: 2020-07-04 21:57:53
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python_learning\spider\font_anti_crawler\douyu_crawler.py
'''

# font_dict = {'0':0,'2':1,'5':2,'3':3,'1':4,'7':5,'9':6,'8':7,'6':8,'4':9}
#
# for i in '472984':
#     print(font_dict[i])

import requests
from lxml import etree

url = 'https://www.douyu.com/228989'

response = requests.get(url)
tree = etree.HTML(response.text)

print(tree.xpath('/html/body/h1/text()')[0])

import websocket
websocket.create_connection()
