import pymysql

'''
2015.03.09_16:30:00
'''


def get_min(actual_min):
    if actual_min < 12:
        min = '0'
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



if __name__ == '__main__':
    print(get_time('120712', '1537'))