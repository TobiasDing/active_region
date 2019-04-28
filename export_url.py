from fetch_data import conn1
import os
import pymysql

def fetch_datas_for_download(db):

    conn = conn1
    cursor = conn.cursor()

    sql = f'SELECT * FROM {db} where down = 0 and flag = 1'
    cursor.execute(sql)
    data = cursor.fetchall()

    conn.close()

    return data
count = 0
file = open('x_20190423.txt', 'a')
items = fetch_datas_for_download('aaa.ar_x')
for i in items:
    # print(i)
    file.writelines(i[14])
    conn = pymysql.connect(
        host='188.131.245.201',
        user='dingweiqi',
        password='dingweiqi123',
        database='aaa',
        charset='utf8',
        port=32001)
    cursor = conn.cursor()
    print(i[0])
    sql = f'UPDATE aaa.ar_x SET down=2 where id={i[0]}'
    cursor.execute(sql)
    conn.commit()
    data = cursor.fetchall()

    conn.close()

    file.writelines('\n')



file.close()