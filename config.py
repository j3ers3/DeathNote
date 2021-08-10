# encoding:utf8
# 配置文件，方便直接调用已准备好的C2
# 
#

LHOST = "1.1.1.1"
LPORT = "8880"

port_cs = 8443
port_empire = 8888
port_msf = 4444

# cobalt strite
cs_powershell = "http://{0}:2082/a".format(LHOST)
cs_regsvr32 = "http://{0}:2086/c".format(LHOST)
cs_bitsadmin = "http://{0}:65532/a".format(LHOST)
cs_python = "http://{0}:65533/a".format(LHOST)
cs_hta = "http://{0}/oa/cs.hta".format(LHOST)
cs_exe = "http://{0}/oa/cs.exe".format(LHOST)
cs_dll = "http://{0}/oa/c32.dll".format(LHOST)

# meterpreter/reverse_tcp 
msf_hta = "http://{0}/evil/msf.hta".format(LHOST)
msf_msi = "http://{0}/evil/msi.png".format(LHOST)

# empire
empire_hta = "http://{0}/evil/empire.hta".format(LHOST)

# PowerSploit
ps_url = "http://{}/ps".format(LHOST)
