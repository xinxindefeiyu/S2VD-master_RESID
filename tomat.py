# -*- coding: utf-8 -*-
"""
jpg2mat
"""
import glob
import os
import numpy as np
from PIL import Image
import scipy.io as io

src_dir = '/Users/maweixin/Documents/bishe/data/train/hazy/0001_1/'
save_dir = '/Users/maweixin/Documents/bishe/data/train/hazy/0001/'
file_list = glob.glob(src_dir+'*.jpg')  # get name list of all .jpg files
print('Start...')
# initrialize
numpy_file = []
for file in file_list:
    img = Image.open(file)
    # save to .npy
    res = np.array(img, dtype='uint8')
    print('Saving data...')
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    name = file.split('.')[0].split('/')[-1]
    saved_img =save_dir + name + '.npy'
    np.save(saved_img, res)
    print('Done.')
    numpy_file.append(np.load(saved_img))
    # numpy_file_res = np.expand_dims(np.load(saved_img), axis=3)

result = np.array(numpy_file)
result_transpose = np.transpose(result,(1,2,3,0))

io.savemat('0001.mat', {'data': result_transpose})

