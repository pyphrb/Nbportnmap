from libnmap.process import NmapProcess
import time, datetime
import sys
import os
#from diff_nmap import all_data
ScanIp = sys.argv[1]
today_time = datetime.date.today()
str_today = str(today_time)
filePath = ScanIp
if os.path.exists(filePath):
   os.chdir(filePath)
else:
    os.makedirs(filePath)
    os.chdir(os.getcwd() + os.sep + filePath)
mkdir_file_name = ScanIp + '_' + str_today + '.txt'
#print mkdir_file_name
#sys.exit(0)
nm = NmapProcess( ScanIp, options="-sV")
rc = nm.run()
if nm.rc == 0:
    with open(mkdir_file_name, 'w') as f:
        f.write(nm.stdout)
   #     print 'scan finish'
   # all_data()
else:
    print nm.stderr
