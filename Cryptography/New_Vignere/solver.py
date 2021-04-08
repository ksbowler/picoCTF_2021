enc = "ioffdcjbfjmcifelcaloifgcjecgpgiebpfeiafhgajafkmlfcbpfbioflgcmacg"

key_len = 9
key_temp = []
for k in range(key_len):
	ans1 = ord(enc[k*2]) - ord("a")
	ans2 = ord(enc[k*2+1]) - ord("a")
	temp = []
	for t21 in range(16):
		for t22 in range(16):
			t11 = (ans1-t21)%16
			t12 = (ans1-t21)%16
			c = t11*16+t12
			if chr(c) in "abcdef0123456789": temp.append((t21,t22))

	key_temp.append(temp)
for t in key_temp: print(t)

for j in range(len(key_temp)):
	print(j)
	for key in key_temp[j]:
		ch = True
		for i in range(2*(key_len+j),len(enc),2*key_len):
			t11 = ((ord(enc[i]) - ord("a"))-key[0])%16
			t12 = ((ord(enc[i+1]) - ord("a"))-key[1])%16
			c = t11*16+t12
			if not chr(c) in "abcdef0123456789":
				ch = False
				break
		if ch:
			print(key)

key = [5,9,2,2,0,14,6,15,15]
enc = "ioffdcjbfjmcifelcaloifgcjecgpgiebpfeiafhgajafkmlfcbpfbioflgcmacg"
flag = ""
for i in range(0,len(enc),2):
	ans1 = ord(enc[i]) - ord("a")
	ans2 = ord(enc[i+1]) - ord("a")
	t21 = key[i%9]
	t22 = key[(i+1)%9]
	t11 = (ans1-t21)%16
	t12 = (ans2-t22)%16
	c = t11*16+t12
	flag += chr(c)
print(flag)
