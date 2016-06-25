#!/usr/bin/env python

from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(("127.0.0.1",8899))

s.listen(5)
while True:
	client, addr = s.accept()
	print str(addr)
	client.send("Hello client!".encode('ascii'))
	client.close()
