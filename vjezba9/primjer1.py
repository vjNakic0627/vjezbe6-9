# -*- coding: utf-8 -*-
"""
Created on Sun May 23 20:49:01 2021

@author: IceBear
"""

import socket, ssl, datetime

from local_machine_info import print_machine_info

print("Datum:" , datetime.datetime.now())

host = "127.0.0.1" # Localhost
port = 60000

print_machine_info()
print("**************************************************")

 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server = ssl.wrap_socket(
    server, server_side=True, keyfile="key.pem", certfile="certificate.pem"
)

if __name__ == "__main__":
    server.bind((host, port))
    server.listen(0)

    while True:
        connection, client_address = server.accept()
        while True:
            data = connection.recv(1024)
            if not data:
                break
            print(f"Primljeno: {data.decode('utf-8')}")