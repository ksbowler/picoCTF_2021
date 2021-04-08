from Crypto.Util.number import *
#import sympy
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
HOST, PORT = "mercury.picoctf.net", 6276
s, f = sock(HOST, PORT)
recv_m = read_until(f).split()
flag = str(recv_m[-1])
print(flag)
recv_m = read_until(f).split()
e = int(recv_m[-1])
recv_m = read_until(f).split()
n = int(recv_m[-1])
flag_part = "picoCTF{"
enc = []
len_str = 0

print("for start")
for i in range(len(flag_part)):
	rv = read_until(f,"me: ")
	s.send(flag_part[:i+1].encode()+b"\n")
	recv_m = read_until(f).split()
	enc_str = recv_m[-1]
	#その全体の抽出
	for unt in enc:
		enc_str = enc_str.replace(unt,"")
	enc.append(enc_str)
print("for finish")
for f_p in enc:
	assert f_p in flag
#st = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrtuvwxyz0123456789{}_+-"

#st = "abcdefghijklmnopqrstuvwxyz0123456789"
st = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrtuvwxyz0123456789{}_+-"
#flag = ""
while len(flag_part) < 26:
	for t in st:
		#print(t)
		temp = flag_part + t
		rv = read_until(f,"me: ")
		s.send(temp.encode()+b"\n")
		recv_m = read_until(f).split()
		enc_str = recv_m[-1]
		for unt in enc:
		#k1 = len(enc_str)
			enc_str = enc_str.replace(unt,"")
		#k2 = len(enc_str)
		#assert k1 > k2
	#enc_strがflagに含まれてたらOK
		#print(enc_str)
		if str(enc_str) in str(flag):
			print("find! :",t)
			enc.append(enc_str)
			flag_part += t
			break
	print(flag_part)
	print(len(flag_part))
	

#read_untilの使い方
#返り値があるのでprintするか、何かの変数に入れる
#1行読む：read_until(f)
#特定の文字まで読む：read_until(f,"input")
#配列に格納する：recv_m = read_until(f).split() ot .strip()

#サーバーに何か送るとき
#s.send(b'1\n') : 1を送っている
#バイト列で送ること。str->bytesにするには、変数の後に.encode()
#必ず改行を入れること。終了ポイントが分からなくなる。ex) s.send(flag.encode() + b'\n')

