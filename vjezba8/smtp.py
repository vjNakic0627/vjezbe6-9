# -*- coding: utf-8 -*-
"""
Created on Sun May 23 20:40:06 2021

@author: IceBear
"""

import smtplib
import datetime
import smtpd

SERVER = 'localhost'
PORT = 1025

FROM = "jane.nakic@gmail.com"
TO = ["testtestinski007@gmail.com"]

SUBJECT = "test"

TEXT = "Test " + str(datetime.datetime.now())

message = """\
From: %s
To: %s
Subject: %s
%s
""" % (FROM, ",".join(TO), SUBJECT, TEXT)

server = smtplib.SMTP(SERVER, PORT)
server.sendmail(FROM,TO,message)
server.quit()