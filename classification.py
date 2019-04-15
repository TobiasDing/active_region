import pymysql


conn = pymysql.connect(
    host='localhost',
    user='root',
    password='19950213',
    database='flares',
    charset='utf8',
    port=3306)

cursor = conn.cursor()

with open('/Users/dingweiqi/Documents/2013', 'r') as file:
    lines = file.readlines()
    for line in lines:
        # print(lines[0])
        date1 = line[5:11]
        start = line[13:17]
        finish = line[18:22]
        peak = line[23:27]
        location = line[28:34]
        importance = line[59:60]
        unknown1 = line[61:63]
        unknown2 = line[67:71]
        imp_val = line[72:79]
        num = line[80:85]
        unknown3 = line[86:]
        # print(date1)
        # print(start)
        # print(over)
        # print(peak)
        # print(location)
        # print(importance)
        # print(unknown1)
        # print(unknown2)
        # print(imp_val)
        # print(num)
        # print(unknown3)
        if importance is 'C' or 'M' or 'X':
            if location.isspace():
                continue
            if (int(location[1:3]) <= 30) and (int(location[4:6]) <= 30):
                SQL = '''
                INSERT INTO flares.AR (date1, start, finish, peak, location, importance, unknown1, unknown2, imp_val, num, unknown3)
                VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s); '''
                cursor.execute(SQL,(date1, start, finish, peak, location, importance, unknown1, unknown2, imp_val, num, unknown3))
                conn.commit()
            else:
                continue

        else:
            continue
        print(111)
cursor.close()
conn.close()

