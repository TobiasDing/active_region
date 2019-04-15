import os

data = ['www.baidu.com']

for item in data:
    # os.popen('cd /Users/dingweiqi/Documents/datas')
    # os.chdir("/Users/dingweiqi/Documents/datas");
    tmpres = os.popen('curl -o /Users/dingweiqi/Documents/datas/file.txt %s' % item).readlines()
    print(tmpres)

