# Primjer 2

import threading
import time
import datetime
import socket

exitFlag = 0
def print_machine_info():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print ("Host name: %s" % host_name)
    print ("IP address: %s" % ip_address)
print('Vrijeme pokretanja programa: ' , datetime.datetime.now())
print('Program se izvodi na ovom računalu: ')
print_machine_info()

print('--------------------------------------------------------------')



class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("Pokrecem nit " + self.name)
        print_time(self.name, 5, self.counter)
        print ("Izlazim iz niti " + self.name)
def print_time(threadName, counter, delay):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -=1

#Kreiraj nove niti
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

#Pokreni nove niti
thread1.start()
thread2.start()

print ("\nIzlazim iz glavne niti\n");