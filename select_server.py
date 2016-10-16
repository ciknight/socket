#!/usr/bin/env python
# -*- coding: utf-8 -*-

import select
import socket
import Queue


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setblocking(False)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('0.0.0.0', 9000))
    server.listen(10)

    inputs = [server]
    outputs = []
    #Outgoing message queues (socket:Queue)
    message_queues = {}
    timeout = 60

    """
    print "inputs: %s" % inputs
    """

    while inputs:
        print "waiting for next event"
        readable, writable, exceptional = select.select(inputs, outputs, inputs, timeout)
        """
        print "readable, writable exceptional is %s, %s, %s" % (readable, writable, exceptional)
        """

        if not (readable or writable or exceptional):
            print "Time out ! "
            break

        for s in readable:
            if s is server:
                """
                print "readable s: %s" % s
                """
                connection, client_address = s.accept()
                print "connection from %s" % client_address[0]
                connection.setblocking(0)
                inputs.append(s)
                message_queues[connection] = Queue.Queue()
            else:
                data = s.recv(1024)
                if data:
                    print "recive %s from %s" % (data, s.getpeername())
                    message_queues[s].put(data)
                    if s not in outputs:
                        outputs.append(s)
                else:
                    print "closed from %s" % client_address
                    if s in outputs:
                        outputs.remove(s)
                    inputs.remove(s)
                    s.close()
                    del message_queues[s]
        for s in writable:
            try:
                next_msg = message_queues[s].get_nowait()
            except Queue.Empty:
                print " " , s.getpeername() , 'queue empty'
                outputs.remove(s)
            else:
                print " sending " , next_msg , " to ", s.getpeername()
                s.send(next_msg)
        for s in exceptional:
            print " exception condition on ", s.getpeername()
            if s in outputs:
                outputs.remove(s)
            inputs.remove(s)
            s.close()
            del message_queues[s]


if __name__ == '__main__':
    start_server()
