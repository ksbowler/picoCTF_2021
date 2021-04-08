from Crypto.Util.number import *
#import sympy
from functools import reduce
from operator import mul
from itertools import combinations
import sys
import socket, struct, telnetlib
import hashlib
import string
import math

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

def returnarray(i):
	d = []
	while i > 0:
		d.append(i%64)
		i = i//64
	return d

def PoW(first, second):
	s = string.printable
	print(len(s))
	i = 0
	for k in range(1,1000):
		#k文字の入力
		for j in range(pow(100,len(s))):
			i += 1
			text = first
			ces = returnarray(i)
			for l in range(len(ces)):
				text += s[ces[l]]
			#print(text)
			hs = hashlib.md5(text.encode()).hexdigest()
			#print(hs[:5],hs[-6:])
			if hs[-6:] == second:
				print(hs)
				print(text)
				return text
		
	#return "test"
		
	
#HOSTはIPアドレスでも可
HOST, PORT = "mercury.picoctf.net", 47414
s, f = sock(HOST, PORT)
recv_m = read_until(f).split()
#for i in range(len(recv_m)):
#	print(i,recv_m[i])
first = recv_m[6][1:-1]
second = recv_m[-1]
print(first,second)
text = PoW(first,second)
s.send(text.encode()+b'\n')
recv_m = read_until(f).split()
n = int(recv_m[-1])
print(recv_m)
#print(sympy.factorint(n))
recv_m = read_until(f).split()
e = int(recv_m[-1])
print(recv_m)
m = 12345
maxD = 1 << 20
print(maxD)
c = pow(m,e,n)
for d_p in range(1,maxD+1):
	if d_p%10000 == 0: print(d_p)
	mm = pow(c,d_p,n)
	dif = mm-m
	if(dif < 0): dif = -dif
	p = math.gcd(dif,n)
	if p != 1:
		#pが判明
		q = n//p
		ans = p+q
		ans = str(ans)
		s.send(ans.encode()+b"\n")
		break
print("for d_p finish")
#print(e)
#ne = str(e).encode() + b"\n"
#s.send(ne)
while True:
	print(read_until(f))
#read_untilの使い方
#返り値があるのでprintするか、何かの変数に入れる
#1行読む：read_until(f)
#特定の文字まで読む：read_until(f,"input")
#配列に格納する：recv_m = read_until(f).split() ot .strip()

#サーバーに何か送るとき
#s.send(b'1\n') : 1を送っている
#バイト列で送ること。str->bytesにするには、変数の後に.encode()
#必ず改行を入れること。終了ポイントが分からなくなる。ex) s.send(flag.encode() + b'\n')

