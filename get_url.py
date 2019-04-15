import requests
import json
import pymysql
from get_time import get_time
import time


conn = pymysql.connect(
    host='localhost',
    user='root',
    password='19950213',
    database='flares',
    charset='utf8',
    port=3306)

cursor = conn.cursor()

sql = 'SELECT * FROM flares.X where flag = 0'
items = cursor.execute(sql)
items = cursor.fetchall()



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
    print(text)

    details = json.loads(text)
    id = details['requestid']
    print(id)

    req_url2 = f'http://jsoc.stanford.edu/cgi-bin/ajax/jsoc_fetch?op=exp_status&requestid={id}'

    time.sleep(400)

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
    req = requests.get(url=req_url2, headers=head)
    print(req.text)
    details = json.loads(req.text)
    file_url = 'http://jsoc.stanford.edu' + details['tarfile'].replace('\\', '')
    number = details['count']
    return  file_url



if __name__ == '__main__':
    a = 1
    for item in items:
        sql_date = item[1]
        sql_start = item[2]
        start, stop = get_time(sql_date, sql_start)

        # print(start)
        # print(stop)
        url = get_url(start, stop)
        sql = f'update flares.X set url = \'{url}\' where date1 = \'{sql_date}\''
        cursor.execute(sql)
        sql = f'update flares.X set flag = 1 where date1 = \'{sql_date}\''
        cursor.execute(sql)
        conn.commit()
        a += 1
        if a > 10:
            break
        cursor.close()
        conn.close()