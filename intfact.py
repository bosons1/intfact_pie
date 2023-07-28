#!/usr/bin/python3
import mariadb
import sys
from primes import primes
from zeros import zeros

def hits(ss, curr):
    curr.execute("SELECT * from zeros where mantissa=\""+str(ss) + "\"")
    res = curr.fetchall()
    return len(res)

def get_zero(ss, curr):
    curr.execute("SELECT mantissa,frac from zeros where mantissa=\""+str(ss)+"\"")
    res = curr.fetchall()
    return res

conn = mariadb.connect(user="root", password="", host="localhost", port=3306, database="intfact")
curr = conn.cursor()
num=str(sys.argv[1])
bnum = str(bin(int(num))[2:])
lb = len(bnum)
f=open("./pi.txt","r")
g=open("./e.txt","r")
f.read(2)
g.read(2)
c = 0
l = len(num)
pos = 0
while c < lb:
    pp = str(f.read(1))
    ee = str(g.read(1))
    nn = num[pos % l]
    ss = pp + nn + ee
    if hits(ss, curr) > 1:
        c = c + 1
    pos = pos + 1
f.close()
g.close()
print(pos)
f = open("./pi.txt","r")
g = open("./e.txt","r")
f.read(2)
g.read(2)
pp = str(f.read(pos))
ee = str(g.read(pos))[::-1]
_pos_ = 0
while _pos_ < pos:
    nn = num[_pos_ % l]
    _p_ = pp[_pos_]
    _e_ = ee[_pos_]
    ss = _p_ + nn + _e_
    prime = int(ss) in primes
    zero = int(ss) in zeros
    input([ss, "prime ", prime, "zero ", zero]) 
    _pos_ = _pos_ + 1
f.close()
g.close()
conn.close()
