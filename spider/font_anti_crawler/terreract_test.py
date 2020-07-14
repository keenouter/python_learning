# -*- coding: utf-8 -*-
# @Time    : 2020/7/4 22:43
# @Author  : G.M
# @FileName: terreract_test.py
# @Software: PyCharm


from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
num_str = pytesseract.image_to_string(Image.open('Snipaste_2020-07-04_22-54-15.png'))
print(num_str)
