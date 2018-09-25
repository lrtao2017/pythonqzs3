#!/usr/bin/env python 
__author__ = "lrtao2010" 

#采用tcp协议进行传输
#有粘包现象，不会丢包

from socket import *
import subprocess
import locale

ip_port = ('127.0.0.1',8080)
back_log = 5
buffer_size = 1024

get_default_locale = locale.getdefaultlocale()[1]  # 获取默认编码

tcp_server = socket(AF_INET,SOCK_STREAM)
tcp_server.bind(ip_port)
tcp_server.listen(back_log)

while True:
    tcp_connect,tcp_addr = tcp_server.accept()
    print('新的客户端连接',tcp_addr)
    while True:
        #接收命名信息
        try:
            cmd_recv = tcp_connect.recv(buffer_size)
            if not cmd_recv :break
            print('收到客户端的命令：',cmd_recv)

            #执行命令，并获取结果
            res = subprocess.Popen(cmd_recv.decode('utf-8'), shell=True,
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

            #发送执行结果
            length = len(cmd_res)
            tcp_connect.send(str(length).encode('utf-8'))
            tcp_connect.send(get_default_locale.encode('utf-8'))

            #接收回执信息，解决粘包现象
            client_ready = tcp_connect.recv(buffer_size)
            if client_ready == b'ready':
                tcp_connect.send(cmd_res)
        except Exception as e:
            print(e)
            break
        # finally:
        #     tcp_connect.close()
