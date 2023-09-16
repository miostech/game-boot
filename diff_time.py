import datetime


def diff_time_logs(date_end, date_start):
    date_time_start = datetime.datetime.strptime(str(date_start), '%Y-%m-%d %H:%M:%S.%f')
    date_time_end = datetime.datetime.strptime(str(date_end), '%d-%m-%Y %H:%M:%S')

    diff_minutes = (date_start - date_time_end).total_seconds() / 60.0

    return diff_minutes
