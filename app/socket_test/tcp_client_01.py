#!/usr/bin/env python 
__author__ = "lrtao2010" 

from socket import *

ip_port = ('127.0.0.1',8080)
back_log = 5
buffer_size = 1024

tcp_client = socket(AF_INET,SOCK_STREAM)
tcp_client.connect(ip_port)

while True:
    cmd = input('>>').strip()
    if not cmd :continue
    if cmd == 'q':break

    tcp_client.send(cmd.encode('utf-8'))

    #解决粘包现象
    #接收返回消息的长度和默认编码
    length = int(tcp_client.recv(buffer_size).decode('utf-8'))
    get_default_locale = tcp_client.recv(buffer_size).decode('utf-8')

    #发送确认消息
    tcp_client.send(b'ready')

    recv_size = 0
    recv_msg = b''
    while recv_size < length:
        recv_msg += tcp_client.recv(buffer_size)
        recv_size = len(recv_msg)
    #recv_msg = tcp_client.recv(buffer_size)
    print('命令执行的结果是：',recv_msg.decode(get_default_locale))

tcp_client.close()



