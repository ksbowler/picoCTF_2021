import string
from Crypto.Util.number import *

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]
print(ALPHABET)
enc = "ihjghbjgjhfbhbfcfjflfjiifdfgffihfeigidfligigffihfjfhfhfhigfjfffjfeihihfdieieih"
enc_array = []
for c in enc:
	enc_array.append(ord(c)-ord("a"))
print(enc_array)
#flag_f = "picoCTF{"
def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	return enc

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

def shift_inverse(alf,k):
	#alf = shift(c,k)の返り値, k = key
	# 目標 -> t1を求める
	t2 = ord(k) - LOWERCASE_OFFSET
	for t1 in range(16):
		if ALPHABET[(t1 + t2) % len(ALPHABET)] == alf:
			#print(t1)
			#t1 = ord(c) - LOWERCASE_OFFSET
			#ord(c) = t1 + LOWERCASE_OFFSET
			return chr(t1 + LOWERCASE_OFFSET)

b16 = b16_encode("abcdefgh")
print(b16)
for k in range(16):
	key = [chr(ord("a")+k)]
	enct = ""
	for i,e in enumerate(enc):
		enct += shift_inverse(e,key[i%(len(key))])
	b16 = enct
	for i in range(0,len(b16),2):
		a = b16[i]
		b = b16[i+1]
		t = (ord(a)-ord("a"))*16+(ord(b)-ord("a"))
		print(chr(t),end="")
	print()
