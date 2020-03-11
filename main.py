import os
from pathlib import Path
from utils import down_file, file_manager, info_manager
import constrants


def modify_repository_content(xml_path):
    """修改repository.xml的文件内容"""
    for_str = '/lxf/'
    to_str = "/{}/".format(info_manager.get_user())
    file_manager.replace_all_str(xml_path, for_str, to_str)


if __name__ == '__main__':

    current_dir = info_manager.get_current_dir_path()

    files_dirname = constrants.FILES_DIR_NAME
    files_dir = os.path.join(current_dir, files_dirname)
    itmstransporter_dir = os.path.join(files_dir, constrants.ITMSTRANSPORTER_ID)
    itmstransporter_zip = os.path.join(files_dir, constrants.ITMSTRANSPORTER_ID + ".zip")

    # print(itmstransporter_dir)
    # print(itmstransporter_zip)

    url = constrants.ITMSTRANSPORTER_DOWNLOAD_URL

    if not os.path.exists(files_dir):
        os.mkdir(files_dir)

    if Path(itmstransporter_dir).exists():
        # 存在就删除
        file_manager.remove_dir(itmstransporter_dir)

    # if not Path(itmstransporter_zip).exists():
    # 下载文件
    print('下载文件')
    down_file.download_from_url(url, itmstransporter_zip)

    # 解压
    print('解压文件')
    file_manager.un_zip(itmstransporter_zip, itmstransporter_dir)

    # 修改xml
    print('修改xml')
    xml_filepath = os.path.join(itmstransporter_dir, constrants.REPOSITORY_XML_RELEATIVE_PATH)
    modify_repository_content(xml_filepath)

    # 覆盖itmstransporter目录
    print('覆盖itmstransporter目录')
    dst = os.path.join(info_manager.get_cache_path(), constrants.ITMSTRANSPORTER_ID)
    # print(dst)
    file_manager.remove_dir(dst)
    file_manager.move_file_or_dir(itmstransporter_dir, dst)

    print('执行完成，请重启Transporter，去愉快的上传应用文件吧~')

