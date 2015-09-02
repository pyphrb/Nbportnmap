#/usr/bin/env python
#-*-coding:utf8-*-
#__author__: pyphrb 
# focus web security
#about nmap scan
import os
import Queue
import datetime
import time
from libnmap.process import NmapProcess
from libnmap.parser import NmapParser, NmapParserException
import sys
import re
import logging
import threading
scanResult = []
threads = []
logging.basicConfig(level=logging.DEBUG,\
	format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',\
	datefmt='%a, %d %b %Y %H:%M:%S', filename= 'logs/info.log',filemode='a')
class Mynmap(object):
    def __init__(self, scanIp):
        self.scanIp = scanIp
    def startNmap(self):
        self.nmapScan = NmapProcess(self.scanIp, options='-sV -T4 -A -Pn -p 22-65534')
        self.rc = self.nmapScan.run()
        if self.nmapScan.rc == 0:
        #print self.nmapScan.stdout
            return self.nmapScan.stdout
        else:
            print self.nmapScan.stderr
            logging.info('nmap scan error'+ self.scanIp)
            return False
    def startParse(self):
    #nmap xml parse func
        try:
            self.startNmapScan = self.startNmap()
            if self.startNmap is not False:
                self.parse = NmapParser.parse(self.startNmapScan)
                self.nmapScanreport = self.startReport()
            else:
                sys.exit(0)
        except NmapParserException as e:
                logging.info(e)
                sys.exit(0)
    def startReport(self):
        self.report = self.parse
        if self.report:
            for self.host in self.report.hosts:
                for self.serv in self.host.services:
                    if len(self.serv.banner) and self.serv.state == 'open':
                        scanResult.append((str(self.host.address) + ' ' + '+' + ' ' + 'NmapService: [' +str(self.serv.state) + ' ' + str(self.serv.protocol) + ' ' + "<" + str(self.serv.port) + ">"  + ' ' + str(self.serv.service) + ' ' +  str(self.serv.banner)) + ']')
                    else:
                        if self.serv.state == 'open':
                            scanResult.append((str(self.host.address) + ' ' + '+' + ' ' + 'NmapService: [' + str(self.serv.state) + ' ' + str(self.serv.protocol) + ' ' + "<" + str(self.serv.port) + ">" +  ' ' + str(self.serv.service)) + ']')

class MyThread(threading.Thread):
    def __init__(self, inputi):
        self.inputi = inputi
        threading.Thread.__init__(self)
    def run(self):
        while True:
            if self.inputi.qsize() > 0:
                self.ip = self.inputi.get()
                self.myNmap = Mynmap(self.ip)
                self.myNmap.startParse()
            else:
                break

class Mscan(object):
    @classmethod
    def startNmapScan(cls,list_ip):
        #threadingSum = threading.Semaphore(40)
        q = Queue.Queue(0)
        lists = list_ip
        for ip_list in lists:
            q.put(ip_list)
        for j in range(200):
            threads.append(MyThread(q))
        for x in threads:
            x.start()
        for y in threads:
            y.join()
        return scanResult
    @classmethod
    def getHttp(cls,resultList):
        httpPortList = []
        for line in resultList:
            if 'http' in line.strip():
                if re.search(r"<(.*)>", line.strip()):
                    if re.search(r"\d+\.\d+\.\d+\.\d+", line.strip()):
                        httpPortList.append("http://" + re.search(r"\d+\.\d+\.\d+\.\d+", line.strip()).group(0) + ':' + re.search(r"<(.*)>", line.strip()).group(0).strip('>').lstrip("<") + '/')
                        return httpPortList
