#!/usr/bin/env python
# -*- coding: utf-8 -*-
#author:pyphrb
import os
import datetime
import time
import sys
from compare import compare_data
now_cwd = os.getcwd()
today = datetime.date.today()#gain today time (datetime type)
oneday = datetime.timedelta(days=1)
yesterday = today - oneday
str_today = str(today) + '.txt'
str_yesterday = str(yesterday) + '.txt'
dir_array = []#statement a array
dir_list =  os.listdir(os.getcwd())#gain current directory
for dirFile in dir_list:# foreach array
    if os.path.isdir(dirFile):# assert dirFile is directory
        dir_array.append(dirFile)#if dirFile is directory ,array append
for dirPath in dir_array:# foreach dir_array
        #print dirPath
        # sys.exit(0)
    os.chdir(os.getcwd() + os.sep + dirPath)#change directory to dirPath
    newdata = os.getcwd() + os.sep + dirPath + '_' + str_today
    olddata = os.getcwd() + os.sep + dirPath + '_' + str_yesterday
    if os.path.exists(olddata):
        compare_data(newdata, olddata, dirPath)
    else:
        pass
    os.chdir(now_cwd)
