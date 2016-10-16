#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys
import time
import threading

#sys.stdout = file('recv.log', 'a+')


def worker(client):
    while 1:
        data = None
        try:
            data = client.recv(1024)
            print(data)
            if len(data) == 0 and data == None:
                break
            client.send('recv')
        except:
            break
        time.sleep(2)
    client.close()


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9000))
    server.listen(10)

    while 1:
        client, addr = server.accept()
        print('client %s connetction' % (client))
        threading.Thread(target=worker, args=(client, )).start()


if __name__ == '__main__':
    start_server()
