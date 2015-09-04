<h1 id="nbportnmap-scan-port-banner-tools"><a name="nbportnmap-scan-port-banner-tools" href="#nbportnmap-scan-port-banner-tools"></a>Nbportnmap scan port banner tools</h1>
<h3 id="intorduce-about-tools"><a name="intorduce-about-tools" href="#intorduce-about-tools"></a>intorduce about tools</h3>
<p>you can see the main.py about tools  usage<br>from system import Mscan</p>
<p>resultIpArray = Mscan.startNmapScan(ipList) 这里的ipList example : [‘127.0.0.1’] 这里的startNmapScan返回的是ip端口 返回的list格式如下：</p>
<p>[‘127.0.0.1 + NmapService: [open tcp <22> ssh product: OpenSSH version: 6.0p1 Debian 4+deb7u2 extrainfo: protocol 2.0 ostype: Linux]’, ‘127.0.0.1 + NmapService: [open tcp <80> http product: nginx version: 1.2.4]’, ‘127.0.0.1 + NmapService: [open tcp <9000> tcpwrapped]’]</p>
<p>from system import Mscan</p>
<p>Mscan.getHttp(resultIpArray)</p>
<p>这个函数是返回http web的函数 返回的list [‘<a href="http://127.0.0.1:80/">http://127.0.0.1:80/</a>‘]</p>
<hr class="section">
<p>qq:959297822</p>

