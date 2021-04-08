from Crypto.Util.number import *
#import sympy
from functools import reduce
from operator import mul
from itertools import combinations
import sys
import socket, struct, telnetlib
import zlib

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

st = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz{_}"
#print(len(st))
#HOSTはIPアドレスでも可
HOST, PORT = "mercury.picoctf.net", 29350
s, f = sock(HOST, PORT)
#print(read_until(f,"encrypted: "))
flag = "picoCTF{"
cnt = 0
while True:
	print("flag_part : ",flag)
	kl = read_until(f,"encrypted: ")
	temp = flag + "}\n"
	s.send(temp.encode())
	nonce = read_until(f)
	enc = read_until(f)
	len_temp = int(read_until(f).strip())
	ch = True
	add_str = "}"
	for i in st:
	#print(i)
	#temp = flag + i
	#for j in st:
		kl = read_until(f,"encrypted: ")
		#print(kl)
		temp = flag + i  + "\n"
		s.send(temp.encode())
		nonce = read_until(f)
	#print(nonce)
		enc = read_until(f)
	#print(enc)
		len_enc = int(read_until(f).strip())
		print(i,len_enc)
		if len_enc < len_temp:
			print(temp,i,len_enc)
			add_str = i
	flag += add_str
	if len(zlib.compress(flag.encode('utf-8'))) == 45:
		print(flag)
	print(cnt)
	cnt += 1
	

#read_untilの使い方
#返り値があるのでprintするか、何かの変数に入れる
#1行読む：read_until(f)
#特定の文字まで読む：read_until(f,"input")
#配列に格納する：recv_m = read_until(f).split() ot .strip()

#サーバーに何か送るとき
#s.send(b'1\n') : 1を送っている
#バイト列で送ること。str->bytesにするには、変数の後に.encode()
#必ず改行を入れること。終了ポイントが分からなくなる。ex) s.send(flag.encode() + b'\n')

