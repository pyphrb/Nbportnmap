#!/usr/bin/env python
#-*-coding:utf8-*-
#author: pyphrb
import os
import sys
import threading
import Queue
import time

class Mysystem(threading.Thread):
    
    def __init__(self, inputIp, threadingNum):
	self.inputIp = inputIp
	self.threadingNum = threadingNum
	threading.Thread.__init__(self)
    def run(self):
	with self.threadingNum:
	    self.ip = self.inputIp.get()
	    os.system("python pynmap.py " + self.ip)

if __name__ == "__main__":
    q = Queue.Queue()
    threads = []
    threadingNum = threading.Semaphore(30)
    with open('ip_list.txt', 'r') as f:
	for i in f:
	    ip =  i.strip()
	    q.put(ip)
    f.close()
    for m in range(q.qsize()):
	threads.append(Mysystem(q, threadingNum))
    for x in threads:
	x.start()
    for y in threads:
	y.join()
    os.system("python diff_nmap.py")
	
	    
