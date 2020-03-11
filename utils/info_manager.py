import os, sys
from pathlib import Path

def get_user():
    """获取当前系统用户名"""
    # return getpass.getuser()
    return os.getlogin()


def get_cache_path():
    """获取系统cache路径"""
    return "/Users/{}/Library/Caches".format(get_user())


def is_exe():
    """是否是可执行文件"""
    return sys.argv[0].split('/')[-1].find('.py') == -1


def get_current_dir_path():
    """获取当前执行文件的目录路径"""
    return Path(sys.argv[0]).parent if is_exe() else "{}".format(os.getcwd())


if __name__ == '__main__':
    print(get_cache_path())
