#!/usr/bin/env python3.8

# created by Vu Huu Dung
# Ham read file

#from email.mime.base import MIMEBase
#from email import encoders
import os
import time
from config.check import *
from string import Template


def get_customer_information(filename):
        customer = []

        with open(filename, mode='r', encoding='utf-8') as line:
            for info in line.read().splitlines():
                tmp_info = info.split('||')
                customer.append({'id': tmp_info[0], 'name': tmp_info[1], 'email': tmp_info[2]})

            return customer

def get_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_content:
        tmp_content = template_content.read()
        return Template(tmp_content)

#def get_attachment(filen):
#    # attachment file
#    filename = "File attachment"
#    attachment = open(filen, "rb")
#    part = MIMEBase('application', 'octet-stream')
#    part.set_payload((attachment).read())
#    encoders.encode_base64(part)
#    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
#    return part

#def get_attachment1(filen):
#    # attachment file
#    filename = "File attachment 1"
#    attachment = open(filen, "rb")
#    part = MIMEBase('application', 'octet-stream')
#    part.set_payload((attachment).read())
#    encoders.encode_base64(part)
#    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
#    return part


#def get_file():
#    path ="file/attachment/"
#    listdir = os.listdir(path)
#    for f in listdir:
#        filename = f
#        attachment = open(f"{path}/{f}", "rb")
#        part = MIMEBase('application', 'octet-stream')
#        part.set_payload((attachment).read())
#        encoders.encode_base64(part)
#        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
#    return part