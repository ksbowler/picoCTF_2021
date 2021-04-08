from Crypto.Cipher import DES
import binascii
import itertools
import random
import string
from Crypto.Util.number import *

def pad(msg):
    block_len = 8
    over = len(msg) % block_len
    pad = block_len - over
    return (msg + " " * pad).encode()

def generate_key():
    return pad("".join(random.choice(string.digits) for _ in range(6)))


#FLAG = open("flag").read().rstrip()
KEY1 = generate_key()
#print(KEY1)
#print(pad("test_message"))

enc_flag = b"3d3168deb9f47529b653eb8c8c714edbb45a5810c0d6dc230d35bf812d2e077e055e6644ddfbe422"
enc_flag2 = b"f5e18fe0017c65c2259c173d76b2d997596c8bf467d33c928e09994ed59901d1e6ea074a1fee31dd"
mes = b'746573745f6d657373616765' #b'test_message    '
mmes = binascii.hexlify(b"test_message_abcdefghijklmnopqrstuvwxyz")
#mesもenc_mesもunhexlifyが必要
enc_mes = b"27bab03de2417a99fc28f05b36abb60f"
eenc_mes = b"7cf3f9cffbbef41b1339b0af4455746ac4083649fb83c91bd71e522ec7546ff4e33a3cbf202f724a"
mes = pad(binascii.unhexlify(mes).decode())
#key1 =[608828,608829,608838,608839,608928,608929,608938,608939,609828,609829,609838,609839,609928,609929,609938,487209,609939,618828,618829,618838,618839,618928,618929,618938,618939,619828,619829,619838,619839,619928,619929,619938,619939,708828,708829,708838,708839,708928,708929,708938,708939,709828,709829,709838,709839,709928,709929,709938,709939,718828,718829,718838,718839,718928,718929,718938,718939,719828,719829,719838,719839,719928,719929,719938,719939]
enc_flag = b"33cfb02f33f72122d62212ac27ad166d6a31419f01ac51c7a762c0b3d29391e3c1d5d82a94c3f0df"

ff = open("result2.txt")
aa = ff.readlines()

key1 = []
for key in aa:
	temp = key.split()
	key1.append(temp[1][:-1])
	key2 = temp[-1]
msg = binascii.unhexlify(enc_flag2)
print(msg)
#msg = pad(binascii.unhexlify(enc_flag2).decode())
ll = len(msg)
t = " "*(8-ll%8)
msg += t.encode()
print(msg)
#key2 = 
k2 = pad(str(key2))
print(k2)
for kk in key1:
	k1 = pad(str(kk))
	cipher2 = DES.new(k2, DES.MODE_ECB)
	enc_msg = cipher2.decrypt(msg)
	cipher1 = DES.new(k1, DES.MODE_ECB)
	flag = cipher1.decrypt(enc_msg)
	print(k1,flag)
"""
for i in range(1000000):
	key1 = str(i)
	key1 = "0"*(6-len(key1)) + key1
	k1 = key1
	key1 = pad(key1)
	#print(key1)
	cipher = DES.new(key1, DES.MODE_ECB)
	enc_msg = cipher.encrypt(mes)
	print(bytes_to_long(enc_msg),k1)
	#break
#print("finish")
print("0 0")
for i in range(1000000):
	key2 = str(i)
	key2 = "0"*(6-len(key2)) + key2
	k2 = key2
	key2 = pad(key2)
	cipher = DES.new(key2, DES.MODE_ECB)
	mmes = cipher.decrypt(binascii.unhexlify(enc_mes))
	print(bytes_to_long(mmes),k2)
	#break
print("0 0")
"""
