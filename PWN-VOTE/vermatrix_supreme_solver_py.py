#!/usr/bin/env python3
import sys
import socket
import re
from codecs import decode

seedPat = re.compile(r'^SEED:\s(.+)$')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.settimeout(3.0)
s.connect(('vermatrix.pwn.democrat', 4201))
data = b''
data += s.recv(128)

data = data.decode('utf8')

rows = data.split('\n')

print(data)
print(rows)
print(len(rows))
del(rows[4])

seedMatch = seedPat.match(rows[0]).groups(1)[0]

matrix = rows[1] + ' ' + rows[2] + ' ' + rows[3]
matrix = [int(x) for x in matrix.split(' ')]

print(matrix)
print(type(matrix[0]))
print(seedMatch)
print(type(seedMatch))
g = [x[0] ^ ord(x[1]) for x in zip(matrix,seedMatch)]

z = "{},{},{},{},{},{},{},{},{}\n".format(g[0],g[3],g[6],g[1],g[4],g[7],g[2],g[5],g[8])
z = bytes(z,'ascii')
s.sendall(z)

data = b''
data += s.recv(128)

data = data.decode('utf8')

rows = data.split('\n')

print(data)


