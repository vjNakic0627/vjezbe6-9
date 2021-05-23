# -*- coding: utf-8 -*-
"""
Created on Sun May 23 20:15:38 2021

@author: IceBear
"""

from multiprocessing import Process, Queue
import random

import datetime
import socket

def print_machine_info():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print ("Host name: %s" % host_name)
    print ("IP address: %s" % ip_address)


print("Datum:" , datetime.datetime.now())


print_machine_info()
print("**************************************************")

def rand_num():
    num = random.random()
    print(("\n %f" % num))

if __name__ == '__main__':
    queue = Queue()

    processes = [Process(target=rand_num, args=())]

    for p in processes:
        p.start()

    for p in processes:
        p.join()