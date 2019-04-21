import os
from fetch_data import fetch_datas_for_download
from  fetch_data import download_complete, download_not_complete


while True:
    try:
        data = fetch_datas_for_download()

        url = data[14]
        data_id = data[0]

    except:
        continue
    # os.popen('cd /Users/dingweiqi/Documents/datas')
    # os.chdir("/Users/dingweiqi/Documents/datas");
    # a = os.popen('export all_proxy="socks5://127.0.0.1:1086"').readlines()
    # print(a)

    download_complete(data_id)
    print(f'Start downloading file {data_id} ...')
    print(f'Downloading from {url}')
    try:

        tmpres = os.popen(f'export all_proxy=socks5://127.0.0.1:1086 ; curl -o /Volumes/MobileDisk1/flare/M/tar/{data_id}.tar {url}').readlines()
        print(tmpres)


    except:
        download_not_complete(data_id)
        continue



