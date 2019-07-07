# encoding: utf8
import os
from core.color import *

class Shell:
    def __init__(self):
        self.info = {
            'Name': 'Nmap',
            'Author': 'whois',
            'Update': '2019/5/31',
        }

        self.txt = {
            'ftp_u': '/Pentest/PassList/Passwords/Services/ftp/user.txt',
            'ftp_p': '/Pentest/PassList/Passwords/Services/ftp/password.txt',

            'ssh_u': '/Pentest/PassList/Passwords/Services/ssh/user.txt',
            'ssh_p': '/Pentest/PassList/Passwords/Services/ssh/password.txt',

            'telnet_u': '/Pentest/PassList/Passwords/Services/telnet/user.txt',
            'telnet_p': '/Pentest/PassList/Passwords/Services/telnet/password.txt',

            'mssql_u': '/Pentest/PassList/Passwords/Services/mssql/user.txt',
            'mssql_p': '/Pentest/PassList/Passwords/Services/mssql/pass_nmap_small.txt',
            'mssql_p2': '/Pentest/PassList/Passwords/Services/mssql/pass_hydra.txt',

            'mysql_u': '/Pentest/PassList/Passwords/Services/mysql/user.txt',
            'mysql_p': '/Pentest/PassList/Passwords/Services/mysql/password.txt',

            'oracle_u': '/Pentest/PassList/Passwords/Services/oracle/user.txt',
            'oracle_p': '/Pentest/PassList/Passwords/Services/oracle/password.txt',

            'postgres_u': '/Pentest/PassList/Passwords/Services/pgsql/user.txt',
            'postgres_p': '/Pentest/PassList/Passwords/Services/pgsql/password.txt',

            'mongodb_u': '/Pentest/PassList/Passwords/Services/mongodb/user.txt',
            'mongodb_p': '/Pentest/PassList/Passwords/Services/mongodb/password.txt',

            'rdp_u': '/Pentest/PassList/Passwords/Services/rdp/user.txt',
            'rdp_p': '/Pentest/PassList/Passwords/Services/rdp/password.txt',

            'smb_u': '/Pentest/PassList/Passwords/Services/smb/user.txt',
            'smb_p': '/Pentest/PassList/Passwords/Services/smb/password.txt',

            'vmauthd_u': '/Pentest/PassList/Passwords/Services/vm/user.txt',
            'vmauthd_p': '/Pentest/PassList/Passwords/Services/vm/password.txt',

        }

        self.output = '/Pentest/Scripts/Death/output/'

    def check_ms17_010(self, ip):
        command = "nmap -v -T4 -sV -Pn --open --script smb-vuln-ms17-010 -p445 {0}".format(ip)
        print(red + command + end + "\n")
        os.system(command)


    def check_heartbleed(self, ip):
        command = "nmap -sV -Pn --open --script ssl-heartbleed -p443 {0}".format(ip)
        print(red + command + end + "\n")
        os.system(command)


    def check_dns_zone(self, ip):
        command = "nmap -sV -Pn --open --script dns-zone-transfer -v -p53 {0}".format(ip)
        print(red + command + end + "\n")
        os.system(command)



    def brute(self, ip, port , server, thread=4):
        """
            nmap 对爆破有点差，mssql需要小字典，大了就失败；但是在服务器只有一个nmap时可用。
            hydra对ssh用单线程比较好。
        """
        user_dict = server + '_u'
        pass_dict = server + '_p'

        # 对服务进行判断，取正确的脚本名字
        if server == 'mssql':
            nmap_server = 'ms-sql'
            medusa_server = 'mssql'
        elif server == 'smb':
            medusa_server = 'smbnt'
            nmap_server = 'smb'
        else:
            nmap_server = medusa_server = server

        command = "nmap -sV -Pn --open -oN '{0}brute_{5}.txt' --script {5}-brute --script-args 'userdb={1},passdb={2}' {3} -p{4}".format(self.output, self.txt[user_dict], self.txt[pass_dict], ip, port, nmap_server)

        command2 = "hydra -L {0} -P {1} -f -t {4} -V -s {3} {2} {5}".format(self.txt[user_dict], self.txt[pass_dict], ip, port, thread, server)

        command3 = "medusa -U {0} -P {1} -h {2} -n {3} -M {4} -v 4".format(self.txt[user_dict], self.txt[pass_dict], ip, port, medusa_server)

        print(red + "\n[1] " + blue + command + "\n\n" + red + "[2] " + blue + command2 + "\n\n" + red + "[3] " +blue + command3 + "\n\n" + red + "[4] " + blue + "pass\n" + end )

        choose = input("[=] Please Choose Num: ")

        try:
            if choose == 1:
                os.system(command)
            elif choose == 2:
                os.system(command2)
            elif choose == 3:
                os.system(command3)
            else:
                pass
        except:
            pass

    def map():
        default_port = {
            "ftp": 21,
            "ssh": 22,
            "telnet": 23,
            "smap": 25,
            "rlogin": 513,
            "rsyn": 873,
            "pcanywhere": 5631,
            "mongodb":27017,
            "redis": 6379,
        }
     

    
