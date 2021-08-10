#!/usr/bin/env python3
# encoding:utf8
from core.show_modules import *
from util.util import *
from core.banner import *
from config import *
from future.builtins import input
from modules import powershell_module
from modules import python_module
from modules import linux_module
from modules import mshta_module
from modules import regsvr32_module
from modules import bitsadmin_module
from modules import certutil_module
from modules import msiexec_module
from modules import wmi_module
from modules import msbuild_module
from modules import msf_module
from modules import nmap_module
from modules import tips_module
from modules import persistence_module
from modules import elevate_module
from modules import docker_module

__say__ = """
    渗透测试 备忘录
    
    Pentest Cheat Sheet

    兼容py2和py3
"""


def powershell():
    SHELL = powershell_module.Shell()

    line1 = p_line('Death') + p_line('PSH') + yellow + ' $> '
    line2 = p_line('Death') + p_line('PSH') + green + '[url]' + yellow + ' $> '
    line3 = p_line('Death') + p_line('PSH') + green + '[File url]' + yellow + ' $> '
    line4 = p_line('Death') + p_line('PSH') + green + '[Target ip]' + yellow + ' $> '

    choice = input(line1)

    if choice == '1':
        p_dec(SHELL.desc_reverse)
        listen = input(line2)
        p_pay(SHELL.reverse().format(url=listen)) if listen != '' else p_pay(
            SHELL.reverse().format(url=cs_powershell))

    elif choice == '2':
        p_dec(SHELL.desc_invoke_shellcode)
        p_pay(SHELL.invoke_shellcode())

    elif choice == '3':
        p_dec(SHELL.desc_invoke_dllinjection)
        p_pay(SHELL.invoke_dllinjection())

    elif choice == '4':
        listen = input(line3)
        p_pay(SHELL.downloader().format(url=listen, file=listen.split('/')[-1]))

    elif choice == '5':
        p_pay(SHELL.mimikatz())
        p_pay(SHELL.mimikatz_base64())

    elif choice == '6':
        p_pay(SHELL.powerup_check())
        p_pay(SHELL.powerup_add_user())

    elif choice == '7':
        p_dec(SHELL.desc_portscan)
        listen = input(line4)
        p_pay(SHELL.portscan().format(ps_url=ps_url, ip=listen))

    elif choice == '8':
        p_dec(SHELL.desc_keystrokes)

    elif choice == 'back':
        main()

    elif choice in ('9', 'exit', 'quit', 'q'):
        bye()

    elif choice == 'list':
        show_powershell_modules()

    elif choice == 'info':
        print(SHELL.info)

    elif choice == 'help':
        help()

    elif choice == 'banner':
        print_banner()

    elif choice == 'version':
        ver()

    elif choice == 'clear':
        clear()

    elif '!' in choice:
        os.system(choice[1:])

    powershell()


def python():
    SHELL = python_module.Shell()

    line1 = p_line('Death') + p_line('Linux') + p_line('Py') + yellow + ' $> '
    line2 = p_line('Death') + p_line('Linux') + p_line('Py') + green + '[lhost:lport]' + yellow + ' $> '

    choice = input(line1)

    if choice == '1':
        p_dec(SHELL.desc_simple_reverse)
        listen = input(line2)
        try:
            p_pay(SHELL.simple_reverse(LHOST, port_msf) if listen == '' else p_pay(
                SHELL.simple_reverse(listen.split(':')[0], listen.split(':')[1])))
        except Execption as e:
            error("Please input ip:port")

    elif choice == '2':
        p_dec(SHELL.desc_meter_tcp_reverse)
        listen = input(line2)

        if listen == '':
            print("\nUsing default host:{0} and port:{1} !!!\n".format(LHOST, port_msf))
            return_code = SHELL.bcode(LHOST, port_msf)
            p_pay(SHELL.meter_reverse().format(bcode=return_code))
        else:
            try:
                return_code = SHELL.bcode(listen.split(':')[0], listen.split(':')[1])
                p_pay(SHELL.meter_reverse().format(bcode=return_code))
            except Execption as e:
                error("Please input ip:port")

    elif choice == '3':
        p_dec(SHELL.desc_web_delivery)
        p_pay(SHELL.web_delivery())

    elif choice == '4':
        p_pay(SHELL.tty_shell())

    elif choice == 'back':
        linux()

    elif choice in ('5', 'exit', 'quit', 'q'):
        bye()

    elif choice == 'list':
        show_python_modules()

    elif choice == 'info':
        print(SHELL.info)

    elif choice == 'help':
        help()

    elif choice == 'banner':
        print_banner()

    elif choice == 'clear':
        clear()

    elif choice == 'version':
        ver()

    elif '!' in choice:
        os.system(choice[1:])

    python()


def linux():
    SHELL = linux_module.Shell()

    line1 = p_line('Death') + p_line('Linux') + yellow + ' $> '
    line2 = p_line('Death') + p_line('Linux') + green + '[lhost:lport]' + yellow + ' $> '

    choice = input(line1)

    if choice == '1':
        p_dec(SHELL.desc_reverse)
        listen = input(line2)
        p_pay(SHELL.bash_reverse()) if listen == '' else p_pay(
            SHELL.bash_reverse(listen.split(':')[0], listen.split(':')[1]))

    elif choice == '2':
        p_dec(SHELL.desc_exec_reverse)
        listen = input(line2)
        p_pay(SHELL.exec_reverse()) if listen == '' else p_pay(
            SHELL.exec_reverse(listen.split(':')[0], listen.split(':')[1]))

    elif choice == '3':
        listen = input(line2)
        p_pay(SHELL.perl_reverse()) if listen == '' else p_pay(
            SHELL.perl_reverse(listen.split(':')[0], listen.split(':')[1]))

    elif choice == '4':
        p_dec(SHELL.desc_telnet)
        p_pay(SHELL.telnet_reverse())

    elif choice == '5':
        listen = input(line2)
        p_pay(SHELL.php_reverse()) if listen == '' else p_pay(
            SHELL.php_reverse(listen.split(':')[0], listen.split(':')[1]))

    elif choice == '6':
        listen = input(line2)
        p_pay(SHELL.ruby_reverse()) if listen == '' else p_pay(
            SHELL.ruby_reverse(listen.split(':')[0], listen.split(':')[1]))

    elif choice == '7':
        clear()
        print(banner.py)
        python()

    elif choice == '8':
        p_dec(SHELL.desc_back)
        listen = input(line2)
        p_pay(SHELL.wget_reverse()) if listen == '' else p_pay(
            SHELL.wget_reverse(listen.split(':')[0], listen.split(':')[1]))

    elif choice == '9':
        p_dec(SHELL.linux_tips())

    elif choice == 'back':
        main()

    elif choice in ('10', 'exit', 'quit', 'q'):
        bye()

    elif choice == 'list':
        show_linux_modules()

    elif choice == 'info':
        print(SHELL.info)

    elif choice == 'help':
        help()

    elif choice == 'banner':
        print_banner()

    elif choice == 'clear':
        clear()

    elif choice == 'version':
        ver()

    elif '!' in choice:
        os.system(choice[1:])

    linux()


def mshta():
    SHELL = mshta_module.Shell()

    line = p_line('Death') + p_line('windows') + p_line('mshta') + green + '[url]' + yellow + ' $> ' + end

    p_dec(SHELL.desc_reverse)
    listen = input(line)
    if listen == '':
        print("Using Default Cobalt url\n")
        print("Reverse_https Listen-port {0} with Cobalt".format(port_cs))
        p_pay(SHELL.reverse(cs_hta))
        print("Http Listen-port {0} with Empire".format(port_empire))
        p_pay(SHELL.reverse(empire_hta))
    else:
        say_no() if not listen.startswith('http') else p_pay(SHELL.reverse(listen))


def regsvr32():
    SHELL = regsvr32_module.Shell()

    line = p_line('Death') + p_line('windows') + p_line('regsvr32') + green + '[url]' + yellow + ' $> '

    p_dec(SHELL.desc_reverse)
    p_dec(SHELL.vbs)
    listen = input(line)
    if listen == '':
        print("\nUsing Default Cobalt url")
        p_pay(SHELL.reverse(cs_regsvr32))
    else:
        say_no() if not listen.startswith('http') else p_pay(SHELL.reverse(listen))


def bitsadmin():
    SHELL = bitsadmin_module.Shell()

    line = p_line('Death') + p_line('windows') + p_line('bitsadmin') + green + '[url]' + yellow + ' $> '

    p_dec(SHELL.desc_reverse)
    listen = input(line)
    if listen == '':
        print("\nUsing Default Cobalt url")
        p_pay(SHELL.reverse(cs_bitsadmin, ran_str()))
    else:
        say_no() if not listen.startswith('http') else p_pay(SHELL.reverse(listen, ran_str()))


def msbuild():
    SHELL = msbuild_module.Shell()
    line = p_line('Death') + p_line('windows') + p_line('msbuild') + green + '[shellcode]' + yellow + ' $> '
    p_dec(SHELL.desc_reverse)
    listen = input(line)
    print(SHELL.payload.format(shellcode=listen))


def certutil():
    SHELL = certutil_module.Shell()

    line = p_line('Death') + p_line('windows') + p_line('certutil') + green + '[url]' + yellow + ' $> '

    p_dec(SHELL.desc_reverse)
    listen = input(line)
    if listen == '':
        print("\nUsing Default Cobalt url")
        # good
        p_pay(SHELL.reverse(cs_exe, ran_str()))
        p_pay(SHELL.reverse2(cs_dll, ran_str()))
    else:
        if not listen.startswith('http'):
            error("Please input exe url")
            certutil()
        else:
            p_pay(SHELL.reverse(listen, ran_str()))
            p_pay(SHELL.reverse2(listen, ran_str()))


def msiexec():
    SHELL = msiexec_module.Shell()

    line = p_line('Death') + p_line('windows') + p_line('msiexec') + green + '[url]' + yellow + ' $> '

    p_dec(SHELL.desc_reverse)
    listen = input(line)
    if listen == '':
        print("\nUsing Default Cobalt url")
        print("\npayload=windows/meterpreter/reverse_tcp,lhost={0},lport={1}\n".format(LHOST, port_msf))
        p_pay(SHELL.reverse(msf_msi))
    else:
        if not listen.startswith('http'):
            error("Please input msi url")
            msiexec()
        else:
            p_pay(SHELL.reverse(listen))


def wmi():
    SHELL = wmi_module.Shell()

    line_wmi = p_line('Death') + p_line('windows') + p_line('wmi') + yellow + ' $> '
    line_ip = p_line('Death') + p_line('windows') + p_line('wmi') + green + '[ip]' + yellow + ' $> '
    line_user = p_line('Death') + p_line('windows') + p_line('wmi') + green + '[user]' + yellow + ' $> '
    line_pass = p_line('Death') + p_line('windows') + p_line('wmi') + green + '[password]' + yellow + ' $> '
    line_url = p_line('Death') + p_line('windows') + p_line('wmi') + green + '[url]' + yellow + ' $> '

    choice = input(line_wmi)

    if choice == '1':
        p_dec(SHELL.desc_a)
        ip = input(line_ip)
        good("set ip -> {0}".format(ip))
        user = input(line_user)
        good("set user -> {0}".format(user))
        pwd = input(line_pass)
        good("set password -> {0}".format(pwd))
        p_pay(SHELL.wmi_exec(ip, user, pwd))

    elif choice == '2':
        p_dec(SHELL.desc_mimikatz)
        ip = input(line_ip)
        good("set ip -> {0}".format(ip))
        user = input(line_user)
        good("set ip -> {0}".format(user))
        pwd = input(line_pass)
        good("set ip -> {0}".format(pwd))
        p_pay(SHELL.mimikatz(ip, user, pwd))

    elif choice == '3':
        p_dec(SHELL.desc_reverse)
        url = input(line_url)
        good("set remote_url -> {0}".format(url))
        p_pay(SHELL.reverse(url))

    elif choice == '4':
        p_dec(SHELL.command())

    elif choice == 'back':
        windows()

    elif choice in ('5', 'exit', 'quit', 'q'):
        bye()

    elif choice == 'list':
        show_wmi_modules()

    elif choice == 'info':
        print(SHELL.info)

    elif choice == 'help':
        help()

    elif choice == 'banner':
        print_banner()

    elif choice == 'version':
        ver()

    elif choice == 'clear':
        clear()

    elif '!' in choice:
        os.system(choice[1:])

    wmi()


def windows():
    line = p_line('Death') + p_line('windows') + yellow + ' $> '

    choice = input(line)

    if choice == '1':
        clear()
        print(banner.wmi)
        show_wmi_modules()
        wmi()

    elif choice == '2':
        mshta()

    elif choice == '3':
        regsvr32()

    elif choice == '4':
        bitsadmin()

    elif choice == '5':
        certutil()

    elif choice == '6':
        msiexec()

    elif choice == '7':
        msbuild()

    elif choice == 'help':
        help()

    elif choice == 'back':
        main()

    elif choice in ('8', 'exit', 'quit', 'q'):
        bye()

    elif choice == 'list':
        show_windows_modules()

    elif choice == 'banner':
        print_banner()

    elif choice == 'version':
        ver()

    elif choice == 'clear':
        clear()

    elif '!' in choice:
        os.system(choice[1:])

    windows()


def msfvenom():
    SHELL = msf_module.Shell()

    line = p_line('Death') + p_line('MSFvenom') + yellow + ' $> '
    line2 = p_line('Death') + p_line('MSFvenom')
    line3 = green + '[LHOST:LPORT]' + yellow + ' $> '

    choice = input(line)

    if choice == '1':
        listen = input(line2 + p_line('windows') + line3)
        p_pay(SHELL.meter_re_windows(listen.split(':')[0], listen.split(':')[1])) if listen != '' else say_no()

    elif choice == '2':
        listen = input(line2 + p_line('linux') + line3)
        p_pay(SHELL.meter_re_linux(listen.split(':')[0], listen.split(':')[1])) if listen != '' else say_no()

    elif choice == '3':
        listen = input(line2 + p_line('osx') + line3)
        p_pay(SHELL.meter_re_osx(listen.split(':')[0], listen.split(':')[1])) if listen != '' else say_no()

    elif choice == '4':
        listen = input(line2 + p_line('android') + line3)
        p_pay(SHELL.meter_re_android(listen.split(':')[0], listen.split(':')[1])) if listen != '' else say_no()

    elif choice == '5':
        listen = input(line2 + p_line('webshell') + line3)
        p_pay(SHELL.meter_re_webshell(listen.split(':')[0], listen.split(':')[1])) if listen != '' else say_no()

    elif choice == 'back':
        main()

    elif choice in ('6', 'exit', 'quit', 'q'):
        bye()

    elif choice == 'list':
        show_msf_modules()

    elif choice == 'info':
        print(SHELL.info)

    elif choice == 'help':
        help()

    elif choice == 'banner':
        print_banner()

    elif choice == 'version':
        ver()

    elif '!' in choice:
        os.system(choice[1:])

    msfvenom()


def nmap():
    SHELL = nmap_module.Shell()
    line = p_line('Death') + p_line('Nmap') + yellow + ' $> '
    line_ms17 = p_line('Death') + p_line('Nmap') + p_line('MS17-010') + green + '[IPS]' + yellow + ' $> '
    line_heart = p_line('Death') + p_line('Nmap') + p_line('Heartbleed') + green + '[IPS]' + yellow + ' $> '
    line_dns = p_line('Death') + p_line('Nmap') + p_line('Dns') + green + '[Domain]' + yellow + ' $> '
    line2 = p_line('Death') + p_line('Nmap')
    line3 = green + '[IP:PORT]' + yellow + ' $> '
    line4 = green + '[PORT]' + yellow + ' $> '

    choice = input(line)

    if choice == '1':
        SHELL.check_ms17_010(input(line_ms17))

    elif choice == '2':
        SHELL.check_heartbleed(input(line_heart))

    elif choice == '3':
        SHELL.check_dns_zone(input(line_dns))

    elif choice == '4':
        SHELL.nmap_bootstrap()

    elif choice == '5':
        ip_port = input(line2 + p_line('FTP') + line3)
        SHELL.brute(ip_port.split(':')[0], ip_port.split(':')[1], 'ftp')

    elif choice == '6':
        ip_port = input(line2 + p_line('SSH') + line3)
        SHELL.brute(ip_port.split(':')[0], ip_port.split(':')[1], 'ssh', 1)

    elif choice == '7':
        ip_port = input(line2 + p_line('TELNET') + line3)
        SHELL.brute(ip_port.split(':')[0], ip_port.split(':')[1], 'telnet')

    elif choice == '8':
        ip_port = input(line2 + p_line('MYSQL') + line3)
        SHELL.brute(ip_port.split(':')[0], ip_port.split(':')[1], 'mysql')

    elif choice == '9':
        ip_port = input(line2 + p_line('MSSQL') + line3)
        SHELL.brute(ip_port.split(':')[0], ip_port.split(':')[1], 'mssql')

    elif choice == '10':
        ip_port = input(line2 + p_line('ORACLE') + line3)
        SHELL.brute(ip_port.split(':')[0], ip_port.split(':')[1], 'oracle')

    elif choice == '11':
        ip_port = input(line2 + p_line('POSTGRES') + line3)
        SHELL.brute(ip_port.split(':')[0], ip_port.split(':')[1], 'postgres')

    elif choice == '12':
        ip_port = input(line2 + p_line('MONGODB') + line3)
        SHELL.brute(ip_port.split(':')[0], ip_port.split(':')[1], 'mongodb')

    elif choice == '13':
        ip_port = input(line2 + p_line('REDIS') + line3)
        SHELL.brute(ip_port.split(':')[0], ip_port.split(':')[1], 'redis')

    elif choice == '14':
        ip_port = input(line2 + p_line('VM') + line3)
        SHELL.brute(ip_port.split(':')[0], ip_port.split(':')[1], 'vmauthd')

    elif choice == '15':
        ip_port = input(line2 + p_line('SMB') + line3)
        SHELL.brute(ip_port.split(':')[0], ip_port.split(':')[1], 'smb')

    elif choice == '16':
        ip_port = input(line2 + p_line('RDP') + line3)
        SHELL.brute(ip_port.split(':')[0], ip_port.split(':')[1], 'rdp')

    elif choice == '17':
        print(SHELL.port_list[int(input(line2 + p_line('RDP') + line4))])

    elif choice == 'back':
        main()

    elif choice in ('17', 'exit', 'quit', 'q'):
        bye()

    elif choice == 'list':
        show_nmap_modules()

    elif choice == 'info':
        print(SHELL.info)

    elif choice == 'help':
        help()

    elif choice == 'banner':
        print_banner()

    elif choice == 'version':
        ver()

    elif '!' in choice:
        os.system(choice[1:])

    nmap()


def persistence():
    SHELL = persistence_module.Shell()
    line = p_line('Death') + p_line('Persistence') + yellow + ' $> '

    choice = input(line)

    if choice == '1':
        p_dec(SHELL.SSHKey())

    elif choice == '2':
        p_dec(SHELL.linux_adduser())

    elif choice == '3':
        p_dec(SHELL.Crontab())

    elif choice == '4':
        p_dec(SHELL.Startup())

    elif choice == '5':
        p_dec(SHELL.Ln())

    elif choice == '6':
        p_dec(SHELL.Hide())

    elif choice == '7':
        p_dec(SHELL.Shift())

    elif choice == '8':
        p_dec(SHELL.windows_adduser())

    elif choice == '9':
        p_dec(SHELL.Schtasks())

    elif choice == '10':
        p_dec(SHELL.Startup())

    elif choice == '11':
        p_dec(SHELL.Services())

    elif choice == '12':
        p_dec(SHELL.Reg())

    elif choice == '13':
        pass

    elif choice == 'back':
        main()

    elif choice in ('14', 'exit', 'quit', 'q'):
        bye()

    elif choice == 'list':
        show_persistence_modules()

    elif choice == 'info':
        print(SHELL.info)

    elif choice == 'help':
        help()

    elif choice == 'clear':
        clear()

    elif choice == 'banner':
        print_banner()

    elif choice == 'version':
        ver()

    elif '!' in choice:
        os.system(choice[1:])

    persistence()


def tips():
    SHELL = tips_module.Shell()
    line = p_line('Death') + p_line('Tips') + yellow + ' $> '

    choice = input(line)

    if choice == '1':
        p_dec(SHELL.windows_tips())
    elif choice == '2':
        p_dec(SHELL.one())
    elif choice == '3':
        p_dec(SHELL.two())
    elif choice == '4':
        p_dec(SHELL.three())
    elif choice == '5':
        p_dec(SHELL.scan())
    elif choice == 'back':
        main()

    elif choice in ('6', 'exit', 'quit', 'q'):
        bye()

    elif choice == 'list':
        show_tips_modules()

    elif choice == 'info':
        print(SHELL.info)

    elif choice == 'help':
        help()

    elif choice == 'clear':
        clear()

    elif choice == 'banner':
        print_banner()

    elif choice == 'version':
        ver()

    elif '!' in choice:
        os.system(choice[1:])

    tips()


def elevate_config():
    SHELL = elevate_module.ElevateConfig()
    line = p_line('Death') + p_line('Elevate') + p_line('Config') + yellow + ' $> '
    choice = input(line)

    if choice == '1':
        p_dec(SHELL.service_config_error())
    elif choice == '2':
        p_dec(SHELL.always_Install_elevated())
    elif choice == '3':
        p_dec(SHELL.trusted_service_paths())
    elif choice == '4':
        p_dec(SHELL.auto_install_profile())
    elif choice == '5':
        p_dec(SHELL.scheduled_task())
    elif choice == 'back':
        elevate()
    elif choice in ('6', 'exit', 'quit', 'q'):
        bye()

    elevate_config()


def elevate():
    SHELL = elevate_module.Shell()
    line = p_line('Death') + p_line('Elevate') + yellow + ' $> '

    choice = input(line)

    if choice == '1':
        p_dec(SHELL.kernal())
    elif choice == '2':
        clear()
        show_elevate_config_modules()
        elevate_config()
    elif choice == '3':
        p_dec(SHELL.gpp())
    elif choice == '4':
        p_dec(SHELL.auto_install_profile())
    elif choice == '5':
        p_dec(SHELL.scheduled_task())
    elif choice == 'back':
        main()

    elif choice in ('6', 'exit', 'quit', 'q'):
        bye()

    elif choice == 'list':
        show_elevate_modules()

    elif choice == 'info':
        print(SHELL.info)

    elif choice == 'help':
        help()

    elif choice == 'clear':
        clear()

    elif choice == 'banner':
        print_banner()

    elif choice == 'version':
        ver()

    elif '!' in choice:
        os.system(choice[1:])

    elevate()


def docker():
    SHELL = docker_module.Shell()
    line = p_line('Death') + p_line('Docker') + yellow + ' $> '

    choice = input(line)

    if choice == '1':
        p_dec(SHELL.docker_usage)

    elif choice == '2':
        p_dec(SHELL.docker_is)

    elif choice == '3':
        p_dec(SHELL.docker_remote_api)

    elif choice == '4':
        p_dec(SHELL.k8s_apiserver)

    elif choice == '5':
        p_dec(SHELL.k8s_dashboard)

    elif choice == '6':
        p_dec(SHELL.k8s_kubelet)

    elif choice == '7':
        p_dec(SHELL.k8s_etcd)

    elif choice == 'back':
        main()

    elif choice in ('9', 'exit', 'quit', 'q'):
        bye()

    elif choice == 'list':
        show_docker_modules()

    elif choice == 'info':
        print(SHELL.info)

    elif choice == 'help':
        help()

    elif choice == 'clear':
        clear()

    elif choice == 'banner':
        print_banner()

    elif choice == 'version':
        ver()

    elif '!' in choice:
        os.system(choice[1:])

    docker()


def main():
    line = p_line('Death') + yellow + ' $> '
    main_choice = input(line)

    if main_choice == '1':
        clear()
        print(banner.ghost)
        show_windows_modules()
        windows()

    elif main_choice == '2':
        clear()
        print(banner.linux)
        show_linux_modules()
        linux()

    elif main_choice == '3':
        clear()
        print(banner.ps)
        show_powershell_modules()
        powershell()

    elif main_choice == '4':
        clear()
        print(banner.tips)
        show_tips_modules()
        tips()

    elif main_choice == '5':
        clear()
        print(banner.msfvenom)
        show_msf_modules()
        msfvenom()

    elif main_choice == '6':
        clear()
        print(banner.nmap)
        show_nmap_modules()
        nmap()

    elif main_choice == '7':
        clear()
        print(banner.elevate)
        show_elevate_modules()
        elevate()

    elif main_choice == '8':
        clear()
        print(banner.persistence)
        show_persistence_modules()
        persistence()

    elif main_choice == '9':
        clear()
        print(banner.ghost)
        show_docker_modules()
        docker()

    elif main_choice == 'help':
        print(banner.ban)
        help()

    elif main_choice == 'clear':
        clear()

    elif main_choice == 'banner':
        print_banner()

    elif main_choice == 'list':
        clear()
        print(banner.ban)
        banner_main()
        show_modules()

    elif main_choice == 'version':
        ver()

    elif main_choice in ('9', 'exit', 'quit', 'q'):
        bye()

    elif '!' in main_choice:
        os.system(main_choice[1:])

    main()


def exploit():
    try:
        print(banner.ban)
        banner_main()
        show_modules()
        main()
    except KeyboardInterrupt:
        bye()


if __name__ == '__main__':
    exploit()
