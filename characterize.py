#!/usr/bin/python3
import sys
from primes import primes
from mpmath import zetazero

f=open("./pi.txt","r")
g=open("./e.txt","r")
f.read(2)
g.read(2)
num = str(sys.argv[1])
MAGIC = int(sys.argv[2])
c = 0
l = len(num)
count = 0
hit = 0
while True:
    pp = str(f.read(1))
    nn = num[c % l]
    ee = str(g.read(1))
    ss = str(pp + nn + ee)
    if int(ss) in primes:
        f.seek(2)
        if (c + 1) % l == 0:
            count = count + 1
            if count % l == 0:
                hit = hit + 1
                if hit == MAGIC:
                    c = c + 1
                    break
    c = c + 1
f.close()
g.close()
f=open("./pi.txt","r")
g=open("./e.txt","r")
f.read(2)
g.read(2)
ee = str(g.read(c))[::-1]
pos = 0
t = 1
state = ""
hit = 0
while pos < c:
    nn = num[pos % l]
    pp = str(f.read(1))
    ss = pp + nn + ee[pos]
    if int(ss) in primes:
        state = state + str(t)
        hit = hit + 1
        if hit == 10:
            break
        t = 1
        f.seek(2)
    else:
        t = 1 - t
    pos = pos + 1
print(state)
f.close()
g.close()
