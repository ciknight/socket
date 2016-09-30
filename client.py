#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import string
import socket
import time

CONST_STRING = string.ascii_letters + string.digits


def generate_msg(num=10):
    return ''.join(random.sample(CONST_STRING, num))

start_time = int(time.time())
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8080))
while 1:
    msg = 'client say: %s' % generate_msg()
    client.send(msg)
    time.sleep(0.5)
    data = client.recv(1024)
    print('server response: %s' % data)
    if int(time.time()) - start_time == 10:
        client.send('q')
        break
else:
    client.close()
