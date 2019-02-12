
# !/usr/bin/env python3
# encoding:utf-8

import os

def main():
    path = input("输入文件夹路径（要批量重命名的文件夹）：").strip()
    names_file = input("输入文件（文件名列表所存储的文件）：").strip()
    change_files_name(path, names_file)

def change_files_name(dir, names_file_path):
    files = os.listdir(dir)
    files.sort()
    names_file = open(names_file_path, "r", encoding="utf-8")
    i = 0
    for line in names_file:
        file_name = line.strip().rstrip('\n')
        if i >= len(files):
            return
        cur_file = files[i]
        cur_file_name, cur_file_type = os.path.splitext(cur_file)
        before_full_name = os.path.join(dir, cur_file)
        after_full_name = os.path.join(dir, file_name+cur_file_type)
        os.rename(before_full_name, after_full_name)
        print(line)
        i = i + 1

if __name__ == '__main__':
    main()