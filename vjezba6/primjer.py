# -*- coding: utf-8 -*-
"""
Created on Sun May 23 19:16:17 2021

@author: IceBear
"""

#threading primjer.py
#Mrežno programiranje LABno6 2021

import _thread
import time
import datetime

import socket

def print_machine_info():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print ("Host name: %s" % host_name)
    print ("IP address: %s" % ip_address)


print('Vrijeme pokretanja programa: ' , datetime.datetime.now())
print('Program se izvodi na ovom računalu: ')
print_machine_info()

print('--------------------------------------------------------------')

#Definicija funkcije za nit

def print_time( threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("%s: %s" % ( threadName, time.ctime(time.time())))

#Kreiramo dvije niti
try:
    _thread.start_new_thread( print_time, ("Thread-1", 2 ))
    _thread.start_new_thread( print_time, ("Thread-2", 4 ))
except:
    print("Greska: ne mogu pokrenuti nit!!")

while 1:
    pass