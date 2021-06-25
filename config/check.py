#!/usr/bin/env  python3.8
# created by Vu Huu Dung
# Ham bo sung

import time
from datetime import datetime, timedelta

def check_logsuccess():
    with open('log/send.log', 'r', encoding='utf-8') as file:
        i = 1
        count = 0
        for line in file:
            result = str(i) + '-' + line # lay ra noi dung dong trong file
            a = result.count('Success')
            count += a
            i += 1
        return count

def check_logerror():
    with open('log/send.log', 'r', encoding='utf-8') as file:
        count = 0
        for line in file:
            a = line.count('Error')
            count += a
        return count

def check_error(l):
    with open('log/send.log', 'r', encoding='utf-8') as file, open('log/error.log', 'a+', encoding='utf-8') as error: #'a+'
        count = 0
        for line in file:
            count += 1
            if count < l:
                pass
            else:
                b = line.find("Error", 0)
                if b < 0:
                    pass
                else:
                    error.write(line)

def check_linesum():
    with open('file/template/listmails.txt', 'r', encoding='utf-8') as file:
        count = 0
        for line in file:
            count += 1
        return count

def check_linesum1(sumline, number):
    n = int(sumline) - int(number)
    return n

def check_time(timedelay):
    timenow = time.strftime("%H:%M:%S")
    return str(f"{timenow} ({timedelay}s/1)")

def check_format_seconds_to_hhmmss(seconds):
    timee = {}
    timenow = time.strftime("%H:%M:%S")
    tmp_info = timenow.split(':')
    timee["hour"] =tmp_info[0]
    timee["minute"] =tmp_info[1]
    timee["second"] =tmp_info[2]
    hhmmsss = (int(timee.get('hour')) * 3600) + (int(timee.get('minute')) * 60) + (int(timee.get('second'))) + seconds
    try:
        from itertools import product
    except ImportError:
        def product(*seqs):
            if len(seqs) == 2:
                for s1 in seqs[0]:
                    for s2 in seqs[1]:
                        yield (s1,s2)
            else:
                for s in seqs[0]:
                    for p in product(*seqs[1:]):
                        yield (s,) + p

    hhmmss = {}
    i = 0
    for (h,m,s) in product(range(24),range(60),range(60)):
        hhmmss[i] = "%02d:%02d:%02d" % (h,m,s)
        i += 1
    return hhmmss[hhmmsss]

def check_details(timedelay, idd, sumline):
    i = idd
    logsuccess = int(check_logsuccess())
    logerror = int(check_logerror())

    sumline1 = check_linesum1(sumline,i)
    summail1 = int(sumline1)*timedelay
    s1 = time.strftime("%H:%M:%S", time.gmtime(summail1))
    if sumline1 == 0:
        return str(f"Tổng số: {sumline} email, đã gửi xong!\nĐã gửi thành công: {logsuccess} email, Gửi bị lỗi: {logerror} email.\n")
    else:
        return str(f"Còn lại: {sumline1} email đang chờ gửi, Ước tính còn {s1} giây để gửi hết!\nĐã gửi thành công: {logsuccess} email, Gửi bị lỗi: {logerror} email.\n")