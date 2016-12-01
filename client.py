#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
'''
@author:MrSprint
@file:client.py
@time:2016 16-12-1 下午4:33
'''
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',8081))
print(s.recv(1024).decode('utf-8'))
for data in [b'Sprint', b'Ghost', b'SprintGhost']:
    # 发送数据:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()