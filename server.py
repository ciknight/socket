#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('0.0.0.0', 8080))
server.listen(1)
clientsocket, address = server.accept()
data = ""
while data.strip() != "q":
    data = clientsocket.recv(1024)
    if len(data) == 0:
        print('client disconnect')
        break
    print('recv client msg: %s' % data.strip())
    clientsocket.send('already recv')
else:
    clientsocket.close()
    print('client disconnect')
server.close()
