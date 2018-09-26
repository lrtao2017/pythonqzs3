#!/usr/bin/env python 
__author__ = "lrtao2010" 

#多线程测试

import socketserver

ip_port = ('127.0.0.1',8080)
buffer_size = 1024

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print('connect is: ',self.request)
        print('addr is: ',self.client_address)

        while True:
            try:
                #接收信息
                data = self.request.recv(buffer_size)
                if not data:break
                print('收到的客户端信息为：',data,self.client_address)

                #发送信息
                self.request.sendall(data.upper())
            except Exception as e:
                print(e)
                break

if __name__ == '__main__':
    s = socketserver.ThreadingTCPServer(ip_port,MyServer) #多线程
    #s = socketserver.ForkingTCPServer(ip_port,MyServer) #多进程，消耗资源较大
    s.serve_forever()