import pymysql


def fetch_datas_for_download():
    conn = pymysql.connect(
        host='188.131.245.201',
        user='dingweiqi',
        password='dingweiqi123',
        database='aaa',
        charset='utf8',
        port=32001)

    cursor = conn.cursor()

    sql = 'SELECT * FROM aaa.ar_m where down = 0 and flag = 1'
    cursor.execute(sql)
    data = cursor.fetchone()

    conn.close()

    return data



def download_complete(data_id):
    conn = pymysql.connect(
        host='188.131.245.201',
        user='dingweiqi',
        password='dingweiqi123',
        database='aaa',
        charset='utf8',
        port=32001)

    cursor = conn.cursor()

    sql = f'UPDATE aaa.ar_m SET down = 1 where id = {data_id}'
    cursor.execute(sql)
    conn.commit()
    conn.close()

def download_not_complete(data_id):
    conn = pymysql.connect(
        host='188.131.245.201',
        user='dingweiqi',
        password='dingweiqi123',
        database='aaa',
        charset='utf8',
        port=32001)

    cursor = conn.cursor()

    sql = f'UPDATE aaa.ar_m SET down = 0 where id = {data_id}'
    cursor.execute(sql)
    conn.commit()
    print(f'File {data_id} download failed, reload later! ')
    conn.close()



if __name__ == '__main__':
    print(111)