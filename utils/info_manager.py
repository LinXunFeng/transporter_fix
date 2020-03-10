import os


def get_user():
    """获取当前系统用户名"""
    # return getpass.getuser()
    return os.getlogin()


def get_cache_path():
    """获取系统cache路径"""
    return "/Users/{}/Library/Caches".format(get_user())


if __name__ == '__main__':
    print(get_cache_path())
