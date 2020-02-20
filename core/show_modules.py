# encoding: utf-8
from .color import *

def show_modules():
    p_modules("""
-----------------------------------------------------
[1] Windows Reverse Shell
[2] Linux Reverse Shell                 
[3] PowerShell Attack
[4] Python Reverse Shell 
[5] MSFvenom Payload
[6] Brute Scan
[7] Persistence and Backdoor
[8] Clean up
[9] Exit

-----------------------------------------------------""")


def powershell_modules():
    p_modules("""
-----------------------------------------------------
[1] Reverse Shell
[2] PowerSploit Invoke_Shellcode
[3] Downloader
[4] Mimikatz
[5] PowerUp
[6] Portscan
[7] Keystrokes
[8] Exit

----------------------------------------------------""")


def python_modules():
    p_modules("""
-----------------------------------------------------
[1] Simple Reverse Shell
[2] Meterpreter Reverse Shell
[3] Web_Delivery
[4] TTY Shell
[5] Exit

-----------------------------------------------------""")


def linux_modules():
    p_modules("""
-----------------------------------------------------
[1] Bash Reverse Shell
[2] Exec Reverse Shell
[3] Perl Reverse Shell
[4] Telnet Reverse Shell
[5] PHP Reverse Shell
[6] Ruby Reverse Shell
[7] Wget Download
[8] Exit

-----------------------------------------------------""")


def windows_modules():
    p_modules("""
-----------------------------------------------------
[1] Wmic Attack
[2] Mshta Reverse Shell
[3] Regsvr32 Reverse Shell
[4] Bitsadmin Reverse Shell
[5] Certutil Reverse Shell
[6] Msiexec Reverse Shell
[7] MSBuild Reverse Shell
[9] Exit

-----------------------------------------------------""")


def wmic_modules():
    p_modules("""
-----------------------------------------------------
[1] Remote Command
[2] Remote Command Mimikata
[3] Web_Delivery Shell
[4] Some Local Command
[5] Exit

-----------------------------------------------------""")

'''def other_modules():
    p_modules("""
-----------------------------------------------------
[1] MSBuild
[2] JSC
[3] Regasm
[4] Regsvcs
[5] Exit

-----------------------------------------------------""")
'''

def msf_modules():
    p_modules("""
-----------------------------------------------------
[1] Meterpreter Reverse Windows
[2] Meterpreter Reverse Linux
[3] Meterpreter Reverse OSX
[4] Meterpreter Reverse Android
[5] Meterpreter Reverse Webshell
[6] exit

-----------------------------------------------------""")


def nmap_modules():
    p_modules("""
-----------------------------------------------------
[1] Check MS17-010          [9] Brute Pgsql
[2] Check Heartbleed        [10] Brute Mongodb
[3] Brute FTP               [11] Brute Redis
[4] Brute SSH               [12] Brute Vmauthd
[5] Brute Telnet            [13] Brute SMB
[6] Brute Mysql             [14] Brute RDP
[7] Brute Mssql             [15] What Is Port
[8] Brute Oracle            [16] exit

-----------------------------------------------------""")


def persistence_modules():
    p_modules("""
-----------------------------------------------------
[1] Linux SSHKey            [7] Windows Shift Backdoor
[2] Linux AddUser           [8] Windows AddUser
[3] Linux Crontab           [9] Windows Schtasks
[4] Linux Startup           [10] Windows Startup
[5] Linux ln Backdoor       [11] Windows Services
[6] Hide                    [12] Windows Registry
[14] Exit                   [13] Windows Waitfor

-----------------------------------------------------""")


def clean_up():
    p_modules("""
-----------------------------------------------------
[1] Linux             [7] Windows Shift Backdoor
[2] Linux AddUser           [8] Windows AddUser
[3] Linux Crontab           [9] Windows Schtasks
[4] Linux Startup           [10] Windows Startup
[5] Linux ln Backdoor       [11] Windows Services
[6] Hide                    [12] Windows Registry
[14] Exit                   [13] Windows Waitfor

-----------------------------------------------------""")



