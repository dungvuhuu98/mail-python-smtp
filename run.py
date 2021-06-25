#!/usr/bin/env  python3.8

# created by Vu Huu Dung
# Khai bao thong so ket noi

import pyfiglet
import time
from config.check import *
from config.get import *
from config.main import *
import getpass

ascii_banner = pyfiglet.figlet_format("# SEND MAIL #")
print(ascii_banner)
print("Nhập thông tin kết nối server:")
smtp_address = str(input("\tSMTP SERVER ADDRESS: ")).lower()
smtp_port = int(input("\tSMTP PORT (25/465/587): "))
smtp_encrypt = str(input("\tSMTP ENCRYPT (none/ssl/tls): ")).lower()
mail_login = str(input("\tUSER LOGIN: ")).lower()
mail_password = str(getpass.getpass("\tPASSWORD LOGIN: "))
print("Nhập thông tin liên quan:")
alias = str(input("\tAlias (Bí danh): "))
subject = str(input("\tSubject: "))
timedelay = int(input("\tTime delay: "))
print(" ")
what = str(input("Kiểm tra lại thông tin, bắt đầu gửi? (yes/no): "))
print(" ")

if what == "yes":
    if __name__ == "__main__":
        customers = get_customer_information('file/template/listmails.txt')
        message_template = get_template('file/template/template.html')
        path = "file/attachment/"
        smtp_info = {
                'SMTP_ENCRYPT': smtp_encrypt,
                'SMTP_ADDRESS': smtp_address,
                'SMTP_PORT': smtp_port,
                'MAIL_LOGIN': mail_login,
                'MAIL_PASSWORD': mail_password,
                }
        with Live(table, refresh_per_second=1):
            main(customers, message_template, path, smtp_info, alias, subject, timedelay)
#       check_error()
        print('>>>>>>>>>>>>>>> Everything is done!')
else:
    print("Không gửi thì thôi >.<")

ascii_banner1 = pyfiglet.figlet_format(">>> BYE BYE! <<<")
print(ascii_banner1)