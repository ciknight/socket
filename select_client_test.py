#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

def echo():
    print 'connected...'
    return True

CONST_STR = ['hello world', 'this is test data', 'hello~']

SERVER_ADDRESS = ("127.0.0.1", 9000)

sockets = [socket.socket(socket.AF_INET, socket.SOCK_STREAM) for _ in range(8)]

print "connecting..."
[s.connect(SERVER_ADDRESS) for s in sockets if echo()]

counter = 0

print "sending..."
for msg in CONST_STR:
    for s in sockets:
        counter += 1
        s.send('socket:%d send %s' % (counter, msg))

print "recving..."
for s in sockets:
    data = s.recv(1024)
    if not data:
        s.close()
    print data
