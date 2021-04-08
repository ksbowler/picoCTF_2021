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



enc_flag = b"33cfb02f33f72122d62212ac27ad166d6a31419f01ac51c7a762c0b3d29391e3c1d5d82a94c3f0df" #サーバnc時に貰える暗号化されたフラグ
mes = binascii.hexlify(b"test_message_abcdefghijklmnopqrstuvwxyz") #送った平文を()内にbytes列で入れる
mes = pad(binascii.unhexlify(mes).decode())
enc_mes = binascii.unhexlify(b"e3c5c54114152cb7cc0a06a2681f6d95a46042c79aeef59a6f69e5bc8eebf382691c48e4ffbd3d96")
for i in range(1000000):
	key1 = str(i)
	key1 = "0"*(6-len(key1)) + key1
	k1 = key1
	key1 = pad(key1)
	#print(key1)
	cipher1 = DES.new(key1, DES.MODE_ECB)
	enc_msg = cipher1.encrypt(mes)
	print(bytes_to_long(enc_msg),k1)
	#break
#print("finish")
print("0 0")
for i in range(1000000):
	key2 = str(i)
	key2 = "0"*(6-len(key2)) + key2
	k2 = key2
	key2 = pad(key2)
	cipher2 = DES.new(key2, DES.MODE_ECB)
	mmes = cipher2.decrypt(enc_mes)
	print(bytes_to_long(mmes),k2)
	#break
print("0 0")
