#!/usr/bin/env python
# -*- coding: utf-8 -*-

import select
import socket


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setblocking(False)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('0.0.0.0', 8080))
    server.listen(10)

    inputs = [server]
    outputs = []
    #Outgoing message queues (socket:Queue)
    message_queues = {}
    timeout = 20
    while inputs:
        print "waiting for next event"
        readable, writable, exceptional = select.select(inputs, outputs, inputs, timeout)

        if not (readable and writable and exceptional):
            print "Time out ! "
            break

        for s in readable:
            print s

if __name__ == '__main__':
    start_server()
