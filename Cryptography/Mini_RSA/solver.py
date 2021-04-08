import gmpy2
from Crypto.Util.number import *
f = open("ciphertext")
a = f.readlines()
n = int((a[0].split())[1])
e = 3
c = int((a[3].split())[-1])
for i in range(10000000):
	x,y = gmpy2.iroot(c+(n*i),3)
	if y:
		m = int(x)
		print(long_to_bytes(m),i)
		
