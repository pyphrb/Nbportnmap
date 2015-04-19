import subprocess 
import datetime
import sys
today = datetime.date.today()
str_today_txt = str(today) + '.txt'
f = open(str_today_txt, 'w')
p = subprocess.Popen('python thread_system.py',stdout=subprocess.PIPE, shell=True)  
for line in p.stdout.readlines():
    f.write(line)
f.close()
print 'Scan Finish'
