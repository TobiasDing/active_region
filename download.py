import os

data = ['http://jsoc.stanford.edu/SUM72/D1154071488/S00000/JSOC_20190412_078.tar']

for item in data:
    # os.popen('cd /Users/dingweiqi/Documents/datas')
    # os.chdir("/Users/dingweiqi/Documents/datas");
    # a = os.popen('export all_proxy="socks5://127.0.0.1:1086"').readlines()
    # print(a)
    tmpres = os.popen('export all_proxy="socks5://127.0.0.1:1086" ; curl -o /Users/dingweiqi/Documents/datas/file.tar %s' % item).readlines()
    print(tmpres)
    print(111)
