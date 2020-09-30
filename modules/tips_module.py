class Shell:
    def __init__(self):
        self.info = {
            'Name': '内网信息收集',
            'Author': 'whois',
            'Update': '2020/7/06',
        }

    def Tips(self):
        return """
1. 查询当前用户：query user || qwinsta
2. 查询进程列表：tasklist || wmic process list brief
3. 查询启动项：  wmic startup get command,caption
4. 查询会话：   net session
5. 查询布丁：   wmic qfe get Caption,Description,HotFixID,InstalledOn
"""

    def firewall(self):
        return """
1. 关闭防火墙
    netsh firewall set opmode disable            (<= win2003)
    netsh advfirewall set allprofiles state off   (> win2003)
    
2. 查看防火墙配置
    netsh firewall show config
    
3. 修改防火墙配置
    net firewall add allowedprogram c:\\nc.exe "allow nc" enable         (<= win2003)
    net advfirewall firewall add rule name="pass nc" dir=in action=allow program="C:\\nc.exe"  (> win2003)        

4. 允许3389端口放行
    netsh advfirewall firewall add rule name="Remote Desktop" protocol=TCP dir=in localport=3389 action=allow
    
5. 自定义防火墙日志存储
    netsh advfirewall set currentprofile logging firename "C:\\fw.log"
    
"""