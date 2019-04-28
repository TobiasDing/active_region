import os
import pymysql

name_list = []
files = os.listdir('/Volumes/DWQ')
for file in files :
    name_list.append(file)
# print(name_list)

conn = pymysql.connect(
        host='188.131.245.201',
        user='dingweiqi',
        password='dingweiqi123',
        database='aaa',
        charset='utf8',
        port=32001)

cursor = conn.cursor()

for name in name_list:
    # print(name)
    sql = f"SELECT * FROM aaa.ar_x WHERE url like '%{name}%'"
    cursor.execute(sql)
    data = cursor.fetchone()
    if data == None:
        continue
    num = data[11]
    importance = data[7]
    lat = data[5]
    lng = int(data[6]) + 28
    print(lat)
    print(lng)
    os.rename(f'/Volumes/DWQ/{name}', f'/Volumes/DWQ/{importance}_{num}_{lng}_{lat}.tar')


