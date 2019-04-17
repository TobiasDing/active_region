import pymysql


def fetch_datas_for_download():

    conn = pymysql.connect(
        host='222.197.210.12',
        user='root',
        password='19950213',
        database='aaa',
        charset='utf8',
        port=3306)

    cursor = conn.cursor()

    sql = 'SELECT * FROM aaa.M where down = 0 and flag = 1'
    cursor.execute(sql)
    data = cursor.fetchone()
    conn.close()

    return data



def download_complete(data_id):
    conn = pymysql.connect(
        host='222.197.210.12',
        user='root',
        password='19950213',
        database='aaa',
        charset='utf8',
        port=3306)

    cursor = conn.cursor()

    sql = f'UPDATE aaa.M SET down = 1 where id = {data_id}'
    cursor.execute(sql)
    conn.commit()
    conn.close()

def download_not_complete(data_id):
    conn = pymysql.connect(
        host='222.197.210.12',
        user='root',
        password='19950213',
        database='aaa',
        charset='utf8',
        port=3306)

    cursor = conn.cursor()

    sql = f'UPDATE aaa.M SET down = 0 where id = {data_id}'
    cursor.execute(sql)
    conn.commit()
    print(f'File {data_id} download failed, reload later! ')
    conn.close()



if __name__ == '__main__':
    print(111)