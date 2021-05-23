# -*- coding: utf-8 -*-
"""
Created on Sun May 23 20:26:44 2021

@author: IceBear
"""

import multiprocessing as mp

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

def my_func(x):
    return (x**x) # x na potenciju x

def main():
    pool = mp.Pool(mp.cpu_count())
    result = pool.map(my_func, [4,2,3, 5, 3, 2, 1, 2])
    result_set_2 = pool.map(my_func, [4,6,5,4,6,3,23,4,6])

    print(result)
    print(result_set_2)

if __name__ == "__main__":
    main()