import os
from fetch_data import fetch_datas_for_download
from  fetch_data import download_complete, download_not_complete

datas = fetch_datas_for_download()
while True:
    data = fetch_datas_for_download()
    url = data[14]
    data_id = data[0]
    # os.popen('cd /Users/dingweiqi/Documents/datas')
    # os.chdir("/Users/dingweiqi/Documents/datas");
    # a = os.popen('export all_proxy="socks5://127.0.0.1:1086"').readlines()
    # print(a)
    try :
        download_complete(data_id)
        print(data_id)

        tmpres = os.popen(f'cd /Users/dingweiqi/Documents/datas/M ; export all_proxy=socks5://127.0.0.1:1086 ; curl -o /Users/dingweiqi/Documents/datas/M/{data_id}.tar {url}').readlines()
        print(tmpres)


    except:
        download_not_complete(data_id)
        continue



