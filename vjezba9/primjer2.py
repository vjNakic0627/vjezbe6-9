# -*- coding: utf-8 -*-
"""
Created on Sun May 23 20:50:25 2021

@author: IceBear
"""

import socket
import ssl
import datetime

from local_machine_info import print_machine_info

from primjer1 import host as SERVER_HOST
from primjer1 import port as SERVER_PORT

from time import sleep

HOST = "127.0.0.1" # Localhost
PORT = 60009

print("Datum:" , datetime.datetime.now())


print_machine_info()
print("**************************************************")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

client = ssl.wrap_socket(client, keyfile="key.pem", certfile="certificate.pem")

if __name__ == "__main__":
    client.bind((HOST, PORT))
    client.connect((SERVER_HOST, SERVER_PORT))

    while True:
        client.send("Mrezno programiranje LV9".encode("utf-8"))
        sleep(5)