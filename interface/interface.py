from datetime import datetime
from flask import Flask, request, jsonify
import os
import random
import tensorflow as tf
import cv2
from flask_cors import *
from PIL import Image
import numpy as np
#获取当前位置的绝对路径
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

#上传图片test 接口
@app.route("/upload", methods=[ "POST"])
@cross_origin()
def upload():
    #获取
    f = request.files.get('file')
    random_num=random.randint(0, 100)
    filename = datetime.now().strftime("%Y%m%d%H%M%S") + "_" + str(random_num) + "." + f.filename.rsplit('.', 1)[1]

    #保存
    file_path = basedir + "/static/file/" + filename
    f.save(file_path)
    # 调用模型
    class_names = ['人', '冬瓜', '南瓜', '哈密瓜', '土豆', '大葱', '山楂', '木耳', '杏', '杨梅', '杯子', '枣', '柠檬', '桃', '桌子', '梨', '椅子', '樱桃', '橙子', '海带', '火龙果', '猕猴桃', '玉米', '石榴', '秋葵', '竹笋', '胡萝卜', '苦瓜', '苹果', '茄子', '草莓', '菠菜', '菠萝', '葡萄', '蓝莓', '西兰花', '西瓜', '西红柿', '西葫芦', '豆芽', '豇豆', '豌豆', '辣椒', '金针菇', '香菇', '香菜', '香蕉', '黄瓜']


    model = tf.keras.models.load_model("models/mobilenet_newfruit.h5")

    #图片
    img_init = cv2.imread(file_path)  # 打开图片
    h, w, c = img_init.shape
    scale = 400 / h
    img_init = cv2.resize(img_init, (224, 224))  # 将图片大小调整到224*224用于模型推理
    img = np.asarray(img_init)  # 将图片转化为numpy的数组
    outputs = model.predict(img.reshape(1, 224, 224, 3))  # 将图片输入模型得到结果
    result_index = int(np.argmax(outputs))

    result = class_names[result_index]  # 获得对应的水果名称

    #可以配置成对应外网访问的链接
    my_host = "http://127.0.0.1:5000"
    new_path_file = my_host + "/static/file/" + filename

    if result == "人" or result == "桌子" or result == "椅子" or result == "杯子" :
        data = {"code": "400",  "msg": "请选择果蔬"}
    else:
        data = {"code": "200", "url": new_path_file, "result": result}
    #data = {"code": "200", "url": new_path_file, "result": result}
    payload = jsonify(data)
    return payload, 200
@app.route("/caigou", methods=[ "POST"])
@cross_origin()
def caigou():
    name=request.json.get("name")
    age = request.json.get("age")
    result = "我叫" + name + ",今年" + str(age)  + "岁,是个大佬" + "爱好是学习"
    data = {"msg": "success",  "result": result}
    payload = jsonify(data)
    return payload, 200

if __name__ == '__main__':
    app.run()