# -*- coding = utf8 -*-
# @Author:hggg
# @File:hg_07_多进程复制图片.py
import os
import multiprocessing


def copy_file(file_name, soure_dir, dest_dir):
    # 拼接原文件夹路劲和目标文件夹路劲
    source_path = soure_dir + "/" + file_name
    dest_path = dest_dir + "/" + file_name

    # 打开源文件和目标文件
    with open(source_path, "rb") as sourece_file:
        with open(dest_path, "wb") as dest_file:
            # 循环读取源文件到目标路径
            while True:
                data = sourece_file.read(1024)
                if data:
                    dest_file.write(data)
                else:
                    break


if __name__ == '__main__':
    # 定义源文件夹和目标文件夹
    source_dir = "images"
    dest_dir = "image"
    try:
        # 创建文件夹
        os.mkdir("image")
    except:
        print("目标文件夹已创建")

    # 读取源文件夹的文件列表
    file_list = os.listdir(source_dir)

    # 遍历文件列表实现拷贝
    for file_name in file_list:
        # copy_file(file_name, soure_dir, dest_dir)
        # 使用多进程实现多任务拷贝
        sub_process = multiprocessing.Process(target=copy_file(file_name, source_dir, dest_dir))
        sub_process.start()

