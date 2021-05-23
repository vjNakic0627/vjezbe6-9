# -*- coding: utf-8 -*-
"""
Created on Sun May 23 20:24:42 2021

@author: IceBear
"""

import socket
import datetime

import socket

def print_machine_info():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print ("Host name: %s" % host_name)
    print ("IP address: %s" % ip_address)
    
    
    
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
start_time = datetime.datetime.now()
print('Vrijeme pokretanja programa: ' , datetime.datetime.now())
print('Program se izvodi na ovom računalu: ')
print_machine_info()

print('--------------------------------------------------------------')


hostAddress = input('Molimo unesite adresu hosta: ')
ipAddress = socket.gethostbyname(hostAddress)
print ('Skeniram host: ', hostAddress, ' IP adresa: ', ipAddress)

portNum1 = int(input('Početni port >> '))
portNum2 = int(input('Završni port >> '))

def scanner(port):
    try:
        sk.connect((hostAddress, port))
        return True
    except:
        return False

for portNumber in range(portNum1,portNum2):
    print("Skeniram port: ", portNumber)
    if scanner(portNumber):
        print('Port', portNumber, 'je otvoren')

print ('Skeniranje portova završeno!!!')

end_time = datetime.datetime.now()
print(f"Gotovo za {(end_time-start_time).total_seconds()} sekundi.")
# https://linuxhint.com/python-for-hacking-port-scanner/