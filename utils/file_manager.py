import zipfile
import os
import shutil
from pathlib import Path


def un_zip(file_name, unzip_dir):
    """解压zip文件"""
    tmp_unzip_dir = unzip_dir+"1"
    remove_dir(tmp_unzip_dir)
    remove_dir(unzip_dir)

    zip_file = zipfile.ZipFile(file_name)
    os.mkdir(tmp_unzip_dir)
    for names in zip_file.namelist():
        zip_file.extract(names, tmp_unzip_dir)
    zip_file.close()

    # 重命名
    unzip_dir_name = Path(unzip_dir).name
    dst_dir = os.path.join(tmp_unzip_dir, unzip_dir_name)
    src_dir = os.path.join(tmp_unzip_dir, unzip_dir_name + "-master")
    move_file_or_dir(src_dir, dst_dir)

    # 调整目录
    # 移动
    move_file_or_dir(dst_dir, os.path.join(Path(tmp_unzip_dir).parent, unzip_dir_name))
    # 删除
    shutil.rmtree(tmp_unzip_dir)


def remove_dir(dir):
    """
    清空目录
    :param dir: 目录路径
    """
    if os.path.isdir(dir):
        shutil.rmtree(dir)


def move_file_or_dir(src, dst):
    """移动目录"""
    if not os.path.exists(src):
        # src路径不存在
        return
    if os.path.exists(dst):
        # 删除待覆盖路径
        shutil.rmtree(dst)
    shutil.move(src, dst)


def replace_all_str(file_path, for_str, to_str):
    """
    全文搜索替换或单行替换
    :param file_path: 文件路径
    :param for_str: 要被替换的内容
    :param to_str: 替换之后的内容
    """
    if not os.path.exists(file_path):
        # 文件不存在
        print('文件不存在')
        return
    bak_file_path = file_path+".bak"
    with open(file_path, 'r', encoding='utf-8') as f,  open(bak_file_path, 'w', encoding='utf-8') as f_w:
        lines = f.readlines()
        for line in lines:
            if for_str in line:
                line = line.replace(for_str, to_str)
            f_w.write(line)

    os.remove(file_path)
    os.rename(bak_file_path, file_path)


if __name__ == '__main__':
    # replace_all_str('/Users/lxf/Desktop/repository.xml', '/lxf/', '/lxf111/')
    replace_all_str('/Users/lxf/Desktop/repository.xml', '/lxf111/', '/lxf/')
