import os
from urllib.request import urlopen
import requests
from tqdm import tqdm


def download_from_url(url, dst):
    """
    @param: url to download file
    @param: dst place to put the file
    """
    file_size = int(urlopen(url).info().get('Content-Length', -1))
    if file_size < 0:
        return download_from_url(url, dst)

    if os.path.exists(dst):
        first_byte = os.path.getsize(dst)
    else:
        first_byte = 0
    if first_byte >= file_size:
        return file_size
    header = {"Range": "bytes=%s-%s" % (first_byte, file_size)}
    print(header)
    pbar = tqdm(
        total=file_size, initial=first_byte,
        unit='B', unit_scale=True, desc=url.split('/')[-1])
    req = requests.get(url, headers=header, stream=True)
    with(open(dst, 'ab')) as f:
        for chunk in req.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                pbar.update(1024)
    pbar.update()
    pbar.close()
    return file_size


if __name__ == '__main__':
    url = "https://github.com/LinXunFeng/SwiftyFitsize/archive/master.zip"
    filePath = "{}/files/master.zip".format(os.getcwd())
    # download_from_url(url, filePath)
    print(filePath)

