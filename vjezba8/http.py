# -*- coding: utf-8 -*-
"""
Created on Sun May 23 20:37:10 2021

@author: IceBear
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import datetime

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "Jane Nakic " + datetime.datetime.now()
        self.wfile.write(bytes(message, "utf8"))

with HTTPServer(('', 8000), handler) as server:
    server.serve_forever()