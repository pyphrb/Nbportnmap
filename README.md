from system import Mscan

resultIpArray = Mscan.startNmapScan(ipList)
if ipList = ['127.0.0.1']

will return
['127.0.0.1 + NmapService: [open tcp <22> ssh product: OpenSSH version: 6.0p1 Debian 4 extrainfo: protocol 2.0 ostype: Linux]', '127.0.0.1 + NmapService: [open tcp <25> smtp product: Exim smtpd version: 4.80 hostname: debian]', '127.0.0.1 + NmapService: [open tcp <80> http product: Apache httpd version: 2.2.22 extrainfo: (Debian)]', '127.0.0.1 + NmapService: [open tcp <111> rpcbind]', '127.0.0.1 + NmapService: [open tcp <631> ipp product: CUPS version: 1.5]', '127.0.0.1 + NmapService: [open tcp <3306> mysql product: MySQL version: 5.5.44-0+deb7u1]', '127.0.0.1 + NmapService: [open tcp <6942> unknown]', '127.0.0.1 + NmapService: [open tcp <57981> status version: 1 extrainfo: rpc #100024 highver: 1 proto: rpc rpcnum: 100024 lowver: 1]', '127.0.0.1 + NmapService: [open tcp <63342> unknown]']

from system import Mscan

lists = Mscan.getHttp(resultIpArray)
print lists
will output bellow
['http://127.0.0.1:80/']