import pymysql
import os

conn = pymysql.connect(
        host='188.131.245.201',
        user='dingweiqi',
        password='dingweiqi123',
        database='aaa',
        charset='utf8',
        port=32001)

cursor = conn.cursor()



last_num = 0
ar_list_dir = ('/Users/dingweiqi/Documents/ar_list/')

files = os.listdir(ar_list_dir)

for file in files:
    print(file)

    with open(ar_list_dir + file, 'r') as file:

        lines = file.readlines()
        for line in lines:
            # print(lines[0])
            date1 = line[5:11]
            start = line[13:17]
            finish = line[18:22]
            peak = line[23:27]
            location = line[28:34]
            print(location)
            if location is '':
                continue
            if location[0] == 'S':
                lat = location[1:3]
                if int(lat) > 20:
                    continue

            elif location[0] == 'N':
                lat = '-' + location[1:3]
                if int(lat) < -20:
                    continue

            else:
                continue

            if location[3] == 'E':
                continue
                # lng = location[4:6]
                # if int(lng) > 30:
                #     continue
            elif location[3] == 'W':
                lng = '-' + location[4:6]
                if int(lng) < -50:
                    continue
                # if int(lng) > -20:
                #     continue

            importance = line[59:60]
            if importance is not 'B':
                continue
            unknown1 = line[61:63]
            unknown2 = line[67:71]
            imp_val = line[72:79]

            num = line[80:85]
            if num == last_num:
                continue
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
            print('right')
            last_num = num
            SQL = '''
            INSERT INTO aaa.ar_none (date1, start, finish, peak, lat, lng, importance, unknown1, unknown2, imp_val, num, unknown3, flag, down)
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s); '''
            cursor.execute(SQL,(date1, start, finish, peak, lat, lng, importance, unknown1, unknown2, imp_val, num, unknown3, 0, 0))
            conn.commit()
            print(111)
cursor.close()
conn.close()

