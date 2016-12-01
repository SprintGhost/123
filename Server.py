#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
'''
@author:MrSprint
@file:Server.py
@time:2016 16-12-1 下午4:33
'''
import socket,threading,time

def tcplink(sock,adrr):
    print('Accept new connection from %s:%s...'% addr)
    sock.send(b'welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('hello,%s!'% data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s  close.'% addr)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',8081))
s.listen(5)
print('waiting for connection...')

while True:
    sock,addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()