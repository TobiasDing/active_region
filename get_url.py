import requests
import json
import pymysql

import time





def get_min(actual_min):
    if actual_min < 12:
        min = '00'
    elif actual_min < 24 and actual_min >= 12:
        min = '12'
    elif actual_min < 36 and actual_min >= 24:
        min = '24'
    elif actual_min < 48 and actual_min >= 36:
        min = '36'
    elif actual_min >= 48:
        min = '48'

    return min


def get_two_days_ago_date(year, month, day):
    if int(year) % 4 == 0:
        months = [
            31,  # 0, ignore
            31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
        ]
    else:
        months = [
            31,  # 0, ignore
            31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
        ]

    if int(day) > 2:
        day = f'{int(day) - 2}'
        if int(day) < 10:
            day = '0' + day
        return [year, month, day]
    elif int(day) == 2 :
        if month is not '1':
            day = f'{months[int(month) - 1]}'
            if int(day) < 10 :
                day = '0' + day
            month = f'{int(month) - 1}'
            return [year, month, day]
        elif month is '1':
            year = f'{int(year) - 1}'
            day = f'{31}'
            month = f'{12}'
            return [year, month, day]
    elif int(day) == 1:
        if month is not '1':
            day = f'{months[int(month) - 1] - 1}'
            if int(day) < 10 :
                day = '0' + day
            print(int(month) - 1)
            month = f'{int(month) - 1}'
            return [year, month, day]
        elif month is '1':
            year = f'{int(year) - 1}'
            day = f'{30}'
            month = f'{12}'
            return [year, month, day]


def get_time(date, start):
    year = date[0:2]
    month = date[2:4]
    day = date[4:6]

    hour = start[0:2]
    min = start[2:4]
    min = get_min(int(min))

    stop_time = f'20{year}.{month}.{day}_{hour}:{min}:00'
    year, month, day = get_two_days_ago_date(year, month, day)
    start_time = f'20{year}.{month}.{day}_{hour}:{min}:00'

    return [start_time, stop_time]

req_url = 'http://jsoc.stanford.edu/cgi-bin/ajax/jsocextfetch'

head = {
    'Accept': 'text/javascript, text/html, application/xml, text/xml, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '313',
    'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'jsoc.stanford.edu',
    'Origin': 'http://jsoc.stanford.edu',
    'Referer': 'http://jsoc.stanford.edu/ajax/exportdata.html?ds=hmi.M_720s%5B2015.03.09_16%3A30%3A00_TAI-2015.03.11_16%3A30%3A00_TAI%5D&limit=none',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    'X-Prototype-Version': '1.6.1',
    'X-Requested-With': 'XMLHttpRequest'
}


def get_url(start, stop):
    # print(start)
    # print(stop)
    data = {
        'op': 'exp_request',
        'ds': f'hmi.M_720s[{start}_TAI-{stop}_TAI]',
        'sizeratio': '1',
        'process': 'n=0|no_op',
        'requestor': 'none',
        'notify': 'Tobias.ding@hotmail.com',
        'method': 'url-tar',
        'filenamefmt': 'hmi.M_720s.{T_REC:A}.{CAMERA}.{segment}',
        'format': 'json',
        'protocol': 'FITS,compress Rice',
        'dbhost': 'hmidb2'
    }
    print(data['ds'])

    req = requests.post(url=req_url, data=data)
    text = req.text
    print('--------------------')
    print(text)

    details = json.loads(text)
    id1 = details['requestid']
    # print(id1)
    for i in range(10):
        print(i)
        time.sleep(1)

    req_url2 = f'http://jsoc.stanford.edu/cgi-bin/ajax/jsoc_fetch?op=exp_status&requestid={id1}'

    for i in range(10):
        print(i)
        time.sleep(1)
    req = requests.get('http://jsoc.stanford.edu/cgi-bin/drms_parserecset?spec=http%3A%2F%2Fjsoc.stanford.edu%2Fajax%2Fexportdata.html%3Fds%3Dmdi.Mtarp%255B%255D%26limit%3D20')

    head = {
        'Accept': 'text/javascript, text/html, application/xml, text/xml, */*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Host': 'jsoc.stanford.edu',
        'Referer': 'http://jsoc.stanford.edu/ajax/exportdata.html?ds=hmi.M_720s%5B2015.03.09_16%3A30%3A00_TAI-2015.03.11_16%3A30%3A00_TAI%5D&limit=none',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        'X-Prototype-Version': '1.6.1',
        'X-Requested-With': 'XMLHttpRequest'
    }

    for i in range(400):
        print(i)
        time.sleep(1)
    req = requests.get(url=req_url2, headers=head)
    # print(req.text)
    details = json.loads(req.text)
    file_url = 'http://jsoc.stanford.edu' + details['tarfile'].replace('\\', '')
    number = details['count']
    return  file_url



if __name__ == '__main__':
    a = 1
    conn = pymysql.connect(
        host='188.131.245.201',
        user='dingweiqi',
        password='dingweiqi123',
        database='aaa',
        charset='utf8',
        port=32001)

    cursor = conn.cursor()

    sql = 'SELECT * FROM aaa.ar_x where flag = 0'
    items = cursor.execute(sql)
    print(items)
    # print(items)
    items = cursor.fetchall()
    for item in items:
        print(item)
        id1 = item[0]
        sql_date = item[1]
        if int(sql_date) < 100501 :
            print('early')
            continue
        sql_start = item[2]
        start, stop = get_time(sql_date, sql_start)

        # print(start)
        # print(stop)

        try:
            print('requesting')
            url = get_url(start, stop)

        except:
            print('get_url_failed')
            continue
        print(f"No.{id1} sample's url is {url}")
        sql = f'update aaa.ar_x set url = \'{url}\' where id = {id1}'
        cursor.execute(sql)
        conn.commit()
        sql = f'update aaa.ar_x set flag = 1 where id = \'{id1}\''
        cursor.execute(sql)
        print('Saved!')
        conn.commit()
        a += 1

    cursor.close()
    conn.close()