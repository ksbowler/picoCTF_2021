from Crypto.Util.number import *
import sympy
from functools import reduce
from operator import mul
from itertools import combinations
import sys
import socket, struct, telnetlib

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

	
#HOSTはIPアドレスでも可
HOST, PORT = "mercury.picoctf.net", 41934
s, f = sock(HOST, PORT)
print(read_until(f))
print(read_until(f))
enc_flag= read_until(f).strip()
print(enc_flag)
print(read_until(f))
fl = False
#i = 0
roop = ['3d','19','05','50']
key = []
ren = 0
res = ""
res_list = []
#while True:
print(read_until(f,"encrypt? "))
#temp = "a"*282 + "\n"
temp = "a"*49968+"\n"
s.send(temp.encode())
print(read_until(f))
ans = read_until(f).strip()
#print(ans)
#res_list.append(ans.split("3d19"))
#print(ans,type(ans))
#res += ans
print(read_until(f))
print(read_until(f,"encrypt? "))
temp = "a"*32+"\n"
s.send(temp.encode())
print(read_until(f))
keys = read_until(f).strip()
enc = "0345376e1e5406691d5c076c4050046e4000036a1a005c6b1904531d3941055d"
print("picoCTF{",end="")
for k in range(32):
	key = int(keys[k*2]+keys[k*2+1],16)^ord("a")
	e = int(enc[k*2]+enc[k*2+1],16)^key
	#print(e)
	print(chr(e),end="")
print("}")
#必ず改行を入れること。終了ポイントが分からなくなる。ex) s.send(flag.encode() + b'\n')

