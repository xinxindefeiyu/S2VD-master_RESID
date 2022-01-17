#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# File  : autofenbianlv.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2019/5/14
from glob import glob
from PIL import Image
import os

path = r"/Users/maweixin/Documents/bishe/data/train/gt/004_2/"
img_path = []
for i in os.listdir(path):
    if i.endswith('.jpg'):
        img_path.append(i)
path_save = "/Users/maweixin/Documents/bishe/data/train/gt/a1_Rain/"


a = range(0, len(img_path))
i = 0
for file in img_path:
    name = os.path.join(path_save, "%d.jpg" % a[i])
    im = Image.open(path + file)
    im.thumbnail((640, 480))
    print(im.format, im.size, im.mode)
    im.save(name)
    i += 1
