#!/usr/bin/env python 
__author__ = "lrtao2010"

#多线程测试

import socketserver
import subprocess
import locale

ip_port = ('127.0.0.1',8080)
buffer_size = 1024

get_default_locale = locale.getdefaultlocale()[1]  # 获取默认编码

class MyServer(socketserver.BaseRequestHandler):

    def handle(self):
        print('connect is: ',self.request)
        print('addr is: ',self.client_address)

        while True:
            try:
                #接收命令信息
                cmd_recv = self.request.recv(buffer_size)
                if not cmd_recv:break

                # 执行命令，并获取结果
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

                # 发送执行结果
                length = len(cmd_res)
                self.request.sendall(str(length).encode('utf-8'))
                self.request.sendall(get_default_locale.encode('utf-8'))

                # 接收回执信息，解决粘包现象
                client_ready = self.request.recv(buffer_size)
                if client_ready == b'ready':
                    self.request.sendall(cmd_res)

            except Exception as e:
                print(e)
                break

if __name__ == '__main__':
    socketserver.ThreadingTCPServer.allow_reuse_address = True #实现端口重用
    s = socketserver.ThreadingTCPServer(ip_port,MyServer) #多线程
    #s = socketserver.ForkingTCPServer(ip_port,MyServer) #多进程，消耗资源较大
    s.serve_forever()
