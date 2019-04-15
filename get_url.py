import requests
import json
import pymysql
from get_time import get_time
import time






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
    print(start)
    print(stop)
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
    id1 = details['requestid']
    print(id1)
    time.sleep(10)

    req_url2 = f'http://jsoc.stanford.edu/cgi-bin/ajax/jsoc_fetch?op=exp_status&requestid={id1}'

    time.sleep(10)
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
    time.sleep(400)
    req = requests.get(url=req_url2, headers=head)
    print(req.text)
    details = json.loads(req.text)
    file_url = 'http://jsoc.stanford.edu' + details['tarfile'].replace('\\', '')
    number = details['count']
    return  file_url



if __name__ == '__main__':
    a = 1
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='19950213',
        database='flares',
        charset='utf8',
        port=3306)

    cursor = conn.cursor()

    sql = 'SELECT * FROM flares.M where flag = 0'
    items = cursor.execute(sql)
    items = cursor.fetchall()
    for item in items:
        print(item)
        id1 = item[0]
        sql_date = item[1]
        if int(sql_date) < 100501 :
            continue
        sql_start = item[2]
        start, stop = get_time(sql_date, sql_start)

        # print(start)
        # print(stop)

        try:
            url = get_url(start, stop)
        except:
            continue
        print(url)
        sql = f'update flares.M set url = \'{url}\' where id = {id1}'
        cursor.execute(sql)
        sql = f'update flares.M set flag = 1 where date1 = \'{sql_date}\''
        cursor.execute(sql)
        conn.commit()
        a += 1

    cursor.close()
    conn.close()