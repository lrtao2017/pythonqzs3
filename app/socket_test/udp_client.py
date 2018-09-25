#!/usr/bin/env python 
__author__ = "lrtao2010"

from socket import *
import locale

ip_port = ('127.0.0.1', 8080)
back_log = 5
buffer_size = 1024

udp_client = socket(AF_INET,SOCK_DGRAM)

while True:
    cmd = input('>>').strip()
    if not cmd :continue
    if cmd == 'q':break

    udp_client.sendto(cmd.encode('utf-8'),ip_port)
    get_default_locale  = udp_client.recvfrom(buffer_size) #获取服务器端编码
    cmd_res, addr = udp_client.recvfrom(buffer_size) #获取服务器端发来的命令执行信息
    print('命令执行结果是：',cmd_res.decode(get_default_locale[0].decode('utf-8')))
udp_client.close()

