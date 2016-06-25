#!/usr/bin/env python

from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(("127.0.0.1",8899))
s.send("HTTP")
data = s.recv(1024)
print data
s.close()
