#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import string
import socket
import threading

CONST_STRING = string.ascii_letters + string.digits


def generate_msg(num=10):
    return ''.join(random.sample(CONST_STRING, num))


def worker():
    client = socket.socket()
    client.connect(('127.0.0.1', 9000))
    msg = 'client say: %s' % generate_msg()
    client.send(msg)
    data = client.recv(1024)
    print('server response: %s' % data)
    client.close()


if __name__ == '__main__':
    n = 100
    while n:
        threading.Thread(target=worker).start()
        n -= 1
