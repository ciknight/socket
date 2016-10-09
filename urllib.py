#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket


def GET(url):
    url = url.replace('http://', '')
    host = url.split('/')[0]
    uri = '/' + '/'.join(url.split('/')[1:])
    request = 'GET {} HTTP/1.1\r\nHost: {}\r\n\r\n'.format(uri, host)
    sock = socket.socket()
    sock.connect((host, 80))
    sock.send(request.encode('ascii'))
    response = b''
    chunk = sock.recv(4096)
    while chunk:
        response += chunk
        chunk = sock.recv(4096)

    print response

if __name__ == '__main__':
    GET('http://blog.ibeats.top')
