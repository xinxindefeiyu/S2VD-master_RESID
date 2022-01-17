from hdfs import Client
import argparse
import os


args = argparse.ArgumentParser()
args.add_argument("--target", default="result.zip", help="target file")
args = args.parse_args()

# 设置hadoop连接，连接目录为Output
client=Client("http://172.31.246.52:50070",root="/MaYuanhao/")
# 往子目录output里上传实验结果 args.target
client.upload(os.path.join("./output/",args.target), args.target, overwrite=True)
print("upload finished")