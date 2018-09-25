#!/usr/bin/env python 
__author__ = "lrtao2010" 

#采用udp协议进行传输
#不存在粘包现象，会丢包

from socket import *
import subprocess
import locale

ip_port = ('127.0.0.1', 8080)
back_log = 5
buffer_size = 1024

get_default_locale = locale.getdefaultlocale()[1]  # 获取默认编码

udp_server = socket(AF_INET,SOCK_DGRAM)
udp_server.bind(ip_port)

while True:
    #接收通过UDP协议传输过来的信息
    cmd,addr = udp_server.recvfrom(buffer_size)

    #执行命令，将命令运行结果赋值给cmd_res
    cmd_recv = cmd.decode('utf-8')
    print('收到的命令是:',cmd_recv)
    res = subprocess.Popen(cmd_recv,shell=True,
                           stderr=subprocess.PIPE,
                           stdout=subprocess.PIPE,
                           stdin=subprocess.PIPE)
    err = res.stderr.read()
    if err:
        cmd_res = err
    else:
        cmd_res = res.stdout.read()

    if not cmd_res:
        cmd_res = '执行成功'.encode(get_default_locale)
    #发送命令执行结果前先发送默认编码方法
    udp_server.sendto(get_default_locale.encode('utf-8'),addr)
    udp_server.sendto(cmd_res,addr)


