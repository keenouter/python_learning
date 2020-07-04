'''
@Author: Min.Guo
@Date: 2020-07-04 13:59:42
@LastEditTime: 2020-07-04 14:39:41
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python_learning\Web\flask\flask_test.py
'''

from flask import Flask, escape, render_template, url_for, request
from werkzeug.utils import secure_filename
import os
import sys
from PIL import Image
import pytesseract

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World!"


@app.route('/index/')
def test_index():
    return "Hello index!!"


@app.route("/user/<username>")
def show_name(username=None):
    return render_template('hello.html', name=username)


# tesseract 搭建OCR服务，/ocr,以post传递图片设别，返回识别的信息
@app.route('/ocr', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['image']
        # base_path = os.path.dirname(__file__)  # 当前文件所在路径
        base_path = sys.path[0]  # 项目的根目录 boot_main.py目录
        upload_path = os.path.join(base_path,
                                   secure_filename(f.filename))  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
        f.save(upload_path)
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        ocr_info = pytesseract.image_to_string(Image.open(upload_path))
        os.remove(upload_path)
        return ocr_info


if __name__ == "__main__":
    print(sys.path[0])
    app.run()
