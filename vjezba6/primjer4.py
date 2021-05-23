# -*- coding: utf-8 -*-
"""
Created on Sun May 23 19:40:17 2021

@author: IceBear
"""

import queue
import threading
import time
import datetime
import socket

def print_machine_info():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print ("Host name: %s" % host_name)
    print ("IP address: %s" % ip_address)

exitFlag = 0

print('Vrijeme pokretanja programa: ' , datetime.datetime.now())
print('Program se izvodi na ovom računalu: ')
print_machine_info()

print('--------------------------------------------------------------')

class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print ("Pokrecem nit " + self.name)
        process_data(self.name, self.q)
        print ("Izlazim iz niti " + self.name)

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print ("%s procesuira %s" % (threadName, data))
        else:
            queueLock.release()
            time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["Jedan", "Dva", "Tri", "Cetiri", "Pet"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

# Kreiraj nove niti
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1

# Napuni red cekanja
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# Cekaj da se red cekanja isprazni
while not workQueue.empty():
    pass

# Obavijesti niti da je vrijeme za izlazak
exitFlag = 1

# Cekaj dok se sve niti ne izvrse
for t in threads:
 t.join()
print ("\nIzlazim iz glavne niti\n")