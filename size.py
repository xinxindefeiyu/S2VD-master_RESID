import os

path = './testsets/004_2_hazy/'
img_list = []
for i in os.listdir(path):
    img_list.append(i)
img_list.sort()