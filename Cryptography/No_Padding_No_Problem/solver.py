from Crypto.Util.number import *
#import sympy
from functools import reduce
from operator import mul
from itertools import combinations
import sys
import socket, struct, telnetlib
import gmpy2

# --- common funcs ---
def sock(remoteip, remoteport):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((remoteip, remoteport))
	return s, s.makefile('rw')

def read_until(f, delim='\n'):
	data = ''
	while not data.endswith(delim):
		data += f.read(1)
	return data

from fractions import Fraction

def lsb_decryption_oracle(c, e, n, s, f):
	bounds = [0, Fraction(n)]

	i = 0
	while True:
		i += 1
		#if i%50 == 0: print(i)
		c2 = (c * pow(2, e, n)) % n
		v= read_until(f,"decrypt: ")
		ct = str(c2).encode() + b"\n"
		s.send(ct)
		recv_m = read_until(f).split()
		mm = int(recv_m[-1])
		lsb = mm%2
		if lsb == 1:
			bounds[0] = sum(bounds)/2
		else:
			bounds[1] = sum(bounds)/2
		diff = bounds[1] - bounds[0]
		diff = diff.numerator / diff.denominator
		if i%50 == 0:
			print(i)
			m = bounds[1].numerator / bounds[1].denominator
			msg = long_to_bytes(m)
			print(msg)
		if diff == 0:
			m = bounds[1].numerator / bounds[1].denominator
			return m
		c = c2

#print lsb_decryption_oracle(c, decrypt_lsb)	
"""r = 2
cr = (c * pow(r, e, n)) % n
mr = decrypt(cr, d, n)
mprime = (mr * gmpy.invert(r, n)) % n
print mprime"""
#HOSTはIPアドレスでも可
HOST, PORT = "mercury.picoctf.net", 28517
s, f = sock(HOST, PORT)
print(read_until(f,"k!\n"))
print(read_until(f))
print(read_until(f))
#n
recv_m = read_until(f).split()
n = int(recv_m[-1])
print("n:",n)
recv_m = read_until(f).split()
e = int(recv_m[-1])
print("e:",e)
recv_m = read_until(f).split()
c = int(recv_m[-1])
print("c:",c)
r = 2
while True:
	v= read_until(f,"decrypt: ")
	cr = (c * pow(r, e, n)) % n
	ct = str(cr).encode() + b"\n"
	s.send(ct)
	recv_m = read_until(f).split()
	mm = int(recv_m[-1])
	m = (mm * gmpy2.invert(r, n)) % n
	print(long_to_bytes(m))
#m = lsb_decryption_oracle(c, e, n, s, f)
#print(long_to_bytes(m))

