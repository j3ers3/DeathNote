# encoding: utf-8
from .color import *

def show_modules():
    p_modules("""
-----------------------------------------------------
[1] Windows Reverse Shell
[2] Linux Reverse Shell                 
[3] PowerShell Attack
[4] Python Reverse Shell 
[5] Msfvenom Payload
[6] Persistence
[7] Exit

-----------------------------------------------------""")


def powershell_modules():
    p_modules("""
-----------------------------------------------------
[1] Reverse Shell
[2] PowerSploit Invoke--Shellcode
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
[1] Simple reverse shell => call sh
[2] Using meterpreter reverse shell => socket
[3] Web_delivery
[4] Exit

-----------------------------------------------------""")


def linux_modules():
    p_modules("""
-----------------------------------------------------
[1] Bash reverse shell
[2] Exec reverse shell
[3] Perl reverse shell
[4] Wget reverse shell
[5] Exit

-----------------------------------------------------""")


def windows_modules():
    p_modules("""
-----------------------------------------------------
[1] Wmic Attack
[2] Mshta reverse shell
[3] Regsvr32 reverse shell
[4] Bitsadmin reverse shell
[5] Certutil reverse shell
[6] Msiexec reverse shell
[7] Other 
[8] Exit

-----------------------------------------------------""")


def wmic_modules():
    p_modules("""
-----------------------------------------------------
[1] Remote Command
[2] Remote Command Mimikata
[3] Web_delivery shell
[4] Some Local Command
[5] Exit

-----------------------------------------------------""")


def other_modules():
    p_modules("""
-----------------------------------------------------
[1] MSBuild
[2] JSC
[3] Regasm
[4] Regsvcs
[5] Exit

-----------------------------------------------------""")


def msf_modules():
    p_modules("""
-----------------------------------------------------
[1] Meterpreter reverse windows
[2] Meterpreter reverse linux
[3] Meterpreter reverse osx
[4] Meterpreter reverse android
[5] Meterpreter reverse webshell
[6] exit

-----------------------------------------------------""")

