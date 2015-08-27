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
#todaytime date string
#todayDate  = str(time.strftime('%Y-%m-%d', time.localtime())) 
#todayDateTime = datetime.date.today()
#yesterdayDateTime = str(todayDateTime - datetime.timedelta(days=1))
#todaytime loging log document
#todayDateLog = './data/log/' + str(time.strftime('%Y-%m-%d', time.localtime())) + '.log'
#absTodayDateLog = os.path.abspath(todayDateLog)
logging.basicConfig(level=logging.DEBUG,\
	format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',\
	datefmt='%a, %d %b %Y %H:%M:%S', filename= 'logs/info.log',filemode='a')
class Mynmap(object):
	'''nmap scan class '''
	def __init__(self, scanIp):
		self.scanIp = scanIp

	def startNmap(self):
	#start Nmap scan func
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
				#self.startNmapReport = self.startReport()
			else:
				loging.info(e)
				sys.exit(0)
		except NmapParserException as e:
			print e
			logging.info(e)
			sys.exit(0)

	def startReport(self):
	#nmap report func
		self.report = self.parse
		if self.report:
			for self.host in self.report.hosts:
				#print self.host.address
				for self.serv in self.host.services:
					if len(self.serv.banner) and self.serv.state == 'open':
						scanResult.append((str(self.host.address) + ' ' + '+' + ' ' + 'NmapService: [' +str(self.serv.state) + ' ' + str(self.serv.protocol) + ' ' + "<" + str(self.serv.port) + ">"  + ' ' + str(self.serv.service) + ' ' +  str(self.serv.banner)) + ']')
					else:
						if self.serv.state == 'open':
							scanResult.append((str(self.host.address) + ' ' + '+' + ' ' + 'NmapService: [' + str(self.serv.state) + ' ' + str(self.serv.protocol) + ' ' + "<" + str(self.serv.port) + ">" +  ' ' + str(self.serv.service)) + ']')
	
class MyThread(threading.Thread):#继承threading.Thread
	def __init__(self, inputi, threadingSum):
		self.inputi = inputi
		self.threadingSum = threadingSum
		threading.Thread.__init__(self)
	def run(self):
		with self.threadingSum:
			self.ip = self.inputi.get()
			self.myNmap = Mynmap(self.ip)
			self.myNmap.startParse()


class Mscan(object):
	'''scan调用的类'''
	@classmethod
	def startNmapScan(cls,list_ip):
		#修饰器函数 启动扫描
		threadingSum = threading.Semaphore(40)#设置线程池
		q = Queue.Queue(0)#声明队列
		lists = list_ip
		for ip_list in lists:
			q.put(ip_list)
		for j in range(q.qsize()):
			threads.append(MyThread(q, threadingSum))
		for x in threads:
			x.start()#启动线程
		for y in threads:
			y.join()#主线程等所有线程结束然后结束
		return scanResult#返回扫描，以list方式返回
	@classmethod
	def getHttp(cls,resultList):#判断http端口的函数
		httpPortList = []
		for line in resultList:
			if 'http' in line.strip():
				if re.search(r"<(.*)>", line.strip()):
					if re.search(r"\d+\.\d+\.\d+\.\d+", line.strip()):
						httpPortList.append("http://" + re.search(r"\d+\.\d+\.\d+\.\d+", line.strip()).group(0) + ':' + re.search(r"<(.*)>", line.strip()).group(0).strip('>').lstrip("<") + '/')
		return httpPortList#返回http端口url链接
