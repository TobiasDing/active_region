import pymysql

class ar(object):
    location = [0, 0]
    importance = 0
    start = '00-00-00-00-00'
    num = ''

    def __init__(self, num, start, importance, location):
        self.num = num
        self.start = start
        self.importance = importance
        self.location = location


conn = pymysql.connect(
    host='localhost',
    user='root',
    password='19950213',
    database='flares',
    charset='utf8',
    port=3306)

cursor = conn.cursor()

sql = 'SELECT * FROM flares.X'

cursor.execute(sql)
print('total:', cursor.rowcount)
row = cursor.fetchone()
while row:
    # print(row)
    date = row[0]
    time = row[1]
    importance = row[5]
    loc = row[4]
    if not loc.isspace():
        if (int(loc[1:3]) <= 30) and (int(loc[4:6]) <= 30):
            start = f'{date[0:2]}-{date[2:4]}-{date[4:6]}-{time[0:2]}-{time[2:4]}'
            print(start)
    row = cursor.fetchone()