#!/usr/bin/env python3.8

# created by Vu Huu Dung
# cau hinh gui mail

import time
import os
import rich
import smtplib
import socket
import logging
from config.check import *
from config.main import *
from config.get import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.utils import COMMASPACE, formatdate
from os.path import basename
from email import encoders
from rich import box
from rich.live import Live
from rich.table import Table
from rich.panel import Panel
from rich.console import Console

table = Table(
    "ID",
    "Customer Name",
    "Emails",
    "Status",
    "Time",
    "Details",
    #box=box.SIMPLE
)

def add_row(iddd, customer_name, email, status, ttime, details):
    table.add_row(
            iddd,
            customer_name,
            email,
            status,
            ttime,
            details
        )

def main(customers, message_template, path, smtp_info, alias, subject, timedelay):
    logging.basicConfig(filename='log/send.log', format='%(asctime)s - %(filename)s:%(lineno)d\t %(message)s', filemode='w', level=logging.DEBUG) # filemode='w': ghi de log cu
    if smtp_info.get('SMTP_ENCRYPT', "tls"):
        s = smtplib.SMTP(host=smtp_info.get('SMTP_ADDRESS'), port=smtp_info.get('SMTP_PORT'))
        s.ehlo()
        s.starttls()
    elif smtp_info.get('SMTP_ENCRYPT', "ssl"):
        s = smtplib.SMTP_SSL(host=smtp_info.get('SMTP_ADDRESS'), port=smtp_info.get('SMTP_PORT'))
        s.ehlo()
    else:
        s = smtplib.SMTP(host=smtp_info.get('SMTP_ADDRESS'), port=smtp_info.get('SMTP_PORT'))
        s.ehlo()
    try:
        s.login(smtp_info.get('MAIL_LOGIN'), smtp_info.get('MAIL_PASSWORD'))
        timenow = time.strftime("%H:%M:%S")
        tongline = check_linesum()
        summail = int(tongline)*timedelay
        hhmmss = time.strftime("%H:%M:%S", time.gmtime(summail))
        tt = check_format_seconds_to_hhmmss(summail)
        print(f'>>>>>>>>>>>>>>> Sendmail is running... \n\tTổng số: {tongline} email. \n\tƯớc tính tốn {hhmmss}s để gửi xong hết vào lúc {tt} giây. \n\tTime bắt đầu: {timenow}')
        line = 0
        for customer in customers:
            line += 1
            try:
                customer_name = customer.get('name').lower().title()

                msg = MIMEMultipart()
                message = message_template.substitute(CUSTOMER_NAME=customer_name)
                msg['From'] = "{1} <{0}>".format(smtp_info.get('MAIL_LOGIN'), alias)
                msg['To'] = "{0} <{1}>".format(customer_name, customer.get('email'))
                msg['Subject'] = "{1}".format(customer_name, subject)

                listdir = os.listdir(path)
                for f in listdir:
                    filename = f
                    attachment = open(f"{path}/{f}", "rb")
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload((attachment).read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
                    msg.attach(part)
                msg.attach(MIMEText(message, 'html'))
                s.send_message(msg)
                logging.info("Success: Gui mail cho {0} thanh cong | {1}".format(customer.get('email'), customer.get('id')))
                idd = customer.get('id')
                iddd = str(f"{idd}/{tongline}")
                email = customer.get('email')
                status = "Success"
                details = check_details(timedelay, idd, tongline)
                ttime = check_time(timedelay)
                add_row(iddd, customer_name, email, status, ttime, details)
                del msg
                time.sleep(timedelay)
            except (smtplib.SMTPException, smtplib.SMTPServerDisconnected, smtplib.SMTPResponseException, smtplib.SMTPSenderRefused, smtplib.SMTPRecipientsRefused, smtplib.SMTPDataError, smtplib.SMTPConnectError, smtplib.SMTPHeloError, smtplib.SMTPAuthenticationError) as e:
                logging.debug("Error: Khong the gui mail toi  >> {2}. Chi tiet: {0} | {1}".format(e, customer.get('id'), customer.get('email')))
                check_error(line)
                idd = customer.get('id')
                iddd = str(f"{idd}/{tongline}")
                email = customer.get('email')
                status = "Error"
                details = check_details(timedelay, idd, tongline)
                ttime = check_time(timedelay)
                add_row(iddd, customer_name, email, status, ttime, details)
                time.sleep(timedelay)
#               print(f"{n} | Error: Khong the gui mail toi  >> {m}. Chi tiet: {e}")
        s.quit()
        timenoww = time.strftime("%H:%M:%S")
        print(f"\tTime kết thúc: {timenoww}")
    except (smtplib.SMTPException, smtplib.SMTPServerDisconnected, smtplib.SMTPResponseException, smtplib.SMTPSenderRefused, smtplib.SMTPRecipientsRefused, smtplib.SMTPDataError, smtplib.SMTPConnectError, smtplib.SMTPHeloError, smtplib.SMTPAuthenticationError) as ee:
        print(">>> Haha, loi roi! xem lai ket noi di <<<")
        print(" ")
        print(ee)
        print(" ")
        logging.debug("{0}".format(ee))