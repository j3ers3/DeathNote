# encoding: utf-8
from .color import *


def show_modules():
    p_modules("""
-----------------------------------------------------
[1]  Windows Reverse Shell
[2]  Linux Reverse Shell                 
[3]  PowerShell Cheat Sheet
[4]  AD Cheat Sheet
[5]  MSFvenom Payload
[6]  Brute Cheat Sheet
[7]  Privilege Escalation
[8]  Persistence and Backdoors
[9]  Docker K8S Cheat Sheet
[10] Exit

-----------------------------------------------------""")


def show_powershell_modules():
    p_modules("""
-----------------------------------------------------
[1] Reverse Shell
[2] Invoke_Shellcode
[3] Invoke-DllInjection
[3] Downloader
[4] Mimikatz
[5] PowerUp
[6] Portscan
[7] Keystrokes
[8] Exit

----------------------------------------------------""")


def show_python_modules():
    p_modules("""
-----------------------------------------------------
[1] Simple Reverse Shell
[2] Meterpreter Reverse Shell
[3] Web_Delivery
[4] TTY Shell
[5] Exit

-----------------------------------------------------""")


def show_linux_modules():
    p_modules("""
-----------------------------------------------------
[1] Bash Reverse Shell
[2] Exec Reverse Shell
[3] Perl Reverse Shell
[4] Telnet Reverse Shell
[5] PHP Reverse Shell
[6] Ruby Reverse Shell
[7] Python Reverse Shell 
[8] Wget and Curl
[9] Linux Cheat Sheet
[10] Exit

-----------------------------------------------------""")


def show_windows_modules():
    p_modules("""
-----------------------------------------------------
[1] WMI Attack
[2] Mshta Reverse Shell
[3] Regsvr32 Reverse Shell
[4] Bitsadmin Reverse Shell
[5] Certutil Reverse Shell
[6] Msiexec Reverse Shell
[7] MSBuild Reverse Shell
[8] Exit

-----------------------------------------------------""")


def show_wmi_modules():
    p_modules("""
-----------------------------------------------------
[1] Remote Command
[2] WMI with Mimikatz
[3] Web Delivery
[4] Command
[5] Exit

-----------------------------------------------------""")


def show_msf_modules():
    p_modules("""
-----------------------------------------------------
[1] Meterpreter Reverse Windows
[2] Meterpreter Reverse Linux
[3] Meterpreter Reverse OSX
[4] Meterpreter Reverse Android
[5] Meterpreter Reverse Webshell
[6] Exit

-----------------------------------------------------""")


def show_nmap_modules():
    p_modules("""
-----------------------------------------------------
[1]  Check MS17-010          [10] Brute Oracle
[2]  Check Heartbleed        [11] Brute Pgsql
[3]  Check DnsZone           [12] Brute Mongodb
[4]  Nmap bootstrap          [13] Brute Redis
[5]  Brute FTP               [14] Brute Vmauthd
[6]  Brute SSH               [15] Brute SMB
[7]  Brute Telnet            [16] Brute RDP
[8]  Brute Mysql             [17] What is port
[9]  Brute Mssql             [18] Exit

-----------------------------------------------------""")


def show_tips_modules():
    p_modules("""
-----------------------------------------------------
[1] Windows Gather
[2] 定位域环境｜域控制器｜域管理员
[3] 收集域内用户和管理信息
[4] 收集域内其他信息
[5] 内网扫描 
[6] Exit

-----------------------------------------------------""")


def show_persistence_modules():
    p_modules("""
-----------------------------------------------------
[1]  Linux SSHKey            [7]  Windows Shift Backdoor
[2]  Linux AddUser           [8]  Windows AddUser
[3]  Linux Crontab           [9]  Windows Schtasks
[4]  Linux Startup           [10] Windows Startup
[5]  Linux ln Backdoor       [11] Windows Services
[6]  Hide                    [12] Windows Registry
[15] Exit                    [13] Windows Waitfor
                             [14] 端口复用

-----------------------------------------------------""")


def show_elevate_config_modules():
    p_modules("""
-----------------------------------------------------
[1] 服务配置错误
[2] AlwaysInstallElevated
[3] 可信任服务路径漏洞
[4] 自动安装配置文件
[5] 计划任务
-----------------------------------------------------""")


def show_elevate_modules():
    p_modules("""
-----------------------------------------------------
[1] Windows 内核提权
[2] Windows 系统配置错误提权
[3] Windows 组策略首选项
[4] Windows Bypass UAC
[5] Windows 令牌窃取
[6] Windows 无凭证
[7] Linux 内核提权
[8] Linux SUID
[6] Exit
-----------------------------------------------------""")


def show_docker_modules():
    p_modules("""
-----------------------------------------------------
[1] Docker 常用命令
[2] 判断是否为容器环境
[3] [Vul] Docker Remote API (2375)
[4] [Vul] K8s APIServer (8080 6443)
[5] [Vul] K8s Dashboard 
[6] [Vul] K8s kubelet (10250)
[7] [Vul] K8s etcd (2379)
[8] 容器逃逸
[9] Exit
-----------------------------------------------------""")

