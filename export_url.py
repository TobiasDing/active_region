from fetch_data import conn1




def fetch_datas_for_download(db):

    conn = conn1
    cursor = conn.cursor()

    sql = f'SELECT * FROM {db} where down = 0 and flag = 1'
    cursor.execute(sql)
    data = cursor.fetchall()

    conn.close()

    return data

items = fetch_datas_for_download('aaa.ar_none')
for i in items:
    print(i)