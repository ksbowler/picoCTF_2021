def egcd(a,b):
    '''
    Extended Euclidean Algorithm
    returns x, y, gcd(a,b) such that ax + by = gcd(a,b)
    '''
    u, u1 = 1, 0
    v, v1 = 0, 1
    while b:
        q = a // b
        u, u1 = u1, u - q * u1
        v, v1 = v1, v - q * v1
        a, b = b, a - q * b
    return u, v, a

def gcd(a,b):
    '''
    2.8 times faster than egcd(a,b)[2]
    '''
    a,b=(b,a) if a<b else (a,b)
    while b:
        a,b=b,a%b
    return a

def modInverse(e,n):
    '''
    d such that de = 1 (mod n)
    e must be coprime to n
    this is assumed to be true
    '''
    return egcd(e,n)[0]%n

def totient(p,q):
    '''
    Calculates the totient of pq
    '''
    return (p-1)*(q-1)

def bitlength(x):
    '''
    Calculates the bitlength of x
    '''
    assert x >= 0
    n = 0
    while x > 0:
        n = n+1
        x = x>>1
    return n


def isqrt(n):
    '''
    Calculates the integer square root
    for arbitrary large nonnegative integers
    '''
    if n < 0:
        raise ValueError('square root not defined for negative numbers')
    
    if n == 0:
        return 0
    a, b = divmod(bitlength(n), 2)
    x = 2**(a+b)
    while True:
        y = (x + n//x)//2
        if y >= x:
            return x
        x = y


def is_perfect_square(n):
    '''
    If n is a perfect square it returns sqrt(n),
    
    otherwise returns -1
    '''
    h = n & 0xF; #last hexadecimal "digit"
    
    if h > 9:
        return -1 # return immediately in 6 cases out of 16.

    # Take advantage of Boolean short-circuit evaluation
    if ( h != 2 and h != 3 and h != 5 and h != 6 and h != 7 and h != 8 ):
        # take square root if you must
        t = isqrt(n)
        if t*t == n:
            return t
        else:
            return -1
    
    return -1

def rational_to_contfrac(x,y):
    '''
    Converts a rational x/y fraction into
    a list of partial quotients [a0, ..., an]
    '''
    a = x//y
    pquotients = [a]
    while a * y != x:
        x,y = y,x-a*y
        a = x//y
        pquotients.append(a)
    return pquotients

#TODO: efficient method that calculates convergents on-the-go, without doing partial quotients first
def convergents_from_contfrac(frac):
    '''
    computes the list of convergents
    using the list of partial quotients
    '''
    convs = [];
    for i in range(len(frac)):
        convs.append(contfrac_to_rational(frac[0:i]))
    return convs

def contfrac_to_rational (frac):
    '''Converts a finite continued fraction [a0, ..., an]
     to an x/y rational.
     '''
    if len(frac) == 0:
        return (0,1)
    num = frac[-1]
    denom = 1
    for _ in range(-2,-len(frac)-1,-1):
        num, denom = frac[_]*num+denom, num
    return (num,denom)

import random, sys

def miller_rabin_pass(a, s, d, n):
	''' 
	n is an odd number with
		n-1 = (2^s)d, and d odd
		and a is the base: 1 < a < n-1
	
	returns True iff n passes the MillerRabinTest for a 
	'''
	a_to_power = pow(a, d, n)
	i=0
	#Invariant: a_to_power = a^(d*2^i) mod n
	
	# we test whether (a^d) = 1 mod n
	if a_to_power == 1:
		return True
	
	# we test whether a^(d*2^i) = n-1 mod n
	# 	for 0<=i<=s-1
	while(i < s-1):
		if a_to_power == n - 1:
			return True
		a_to_power = (a_to_power * a_to_power) % n
		i+=1
	
	# we reach here if the test failed until i=s-2	
	return a_to_power == n - 1

def miller_rabin(n):
	'''
	Applies the MillerRabin Test to n (odd)
	
	returns True iff n passes the MillerRabinTest for
	K random bases
	'''
	#Compute s and d such that n-1 = (2^s)d, with d odd
	d = n-1
	s = 0
	while d%2 == 0:
		d >>= 1
		s+=1
	
	#Applies the test K times
	#The probability of a false positive is less than (1/4)^K
	K = 20
	
	i=1
	while(i<=K):
	# 1 < a < n-1
		a = random.randrange(2,n-1)
		if not miller_rabin_pass(a, s, d, n):
			return False
		i += 1

	return True

def gen_prime(nbits):
	'''
	Generates a prime of b bits using the
	miller_rabin_test
	'''
	while True:
			p = random.getrandbits(nbits)
			#force p to have nbits and be odd
			p |= 2**nbits | 1
			if miller_rabin(p):
				return p
				break

def gen_prime_range(start, stop):
	'''
	Generates a prime within the given range
	using the miller_rabin_test
	'''
	while True:
		p = random.randrange(start,stop-1)
		p |= 1
		if miller_rabin(p):
				return p
				break


def getPrimePair(bits=512):
    '''
    genera un par de primos p , q con 
        p de nbits y
        p < q < 2p
    '''
    
    assert bits%4==0
    
    p = gen_prime(bits)
    q = gen_prime_range(p+1, 2*p)
    
    return p,q

def generateKeys(nbits=1024):
    '''
    Generates a key pair
        public = (e,n)
        private = d 
    such that
        n is nbits long
        (e,n) is vulnerable to the Wiener Continued Fraction Attack
    '''
    # nbits >= 1024 is recommended
    assert nbits%4==0
    
    p,q = getPrimePair(nbits//2)
    n = p*q
    phi = totient(p, q)
        
    # generate a d such that:
    #     (d,n) = 1
    #    36d^4 < n
    good_d = False
    while not good_d:
        d = random.getrandbits(nbits//4)
        if (gcd(d,phi) == 1 and 36*pow(d,4) < n):
            good_d = True
                    
    e = modInverse(d,phi)
    return e,n,d

def hack_RSA(e,n):
    '''
    Finds d knowing (e,n)
    applying the Wiener continued fraction attack
    '''
    frac = rational_to_contfrac(e, n)
    convergents = convergents_from_contfrac(frac)
    
    for (k,d) in convergents:
        
        #check if d is actually the key
        if k!=0 and (e*d-1)%k == 0:
            phi = (e*d-1)//k
            s = n - phi + 1
            # check if the equation x^2 - s*x + n = 0
            # has integer roots
            discr = s*s - 4*n
            if(discr>=0):
                t = is_perfect_square(discr)
                if t!=-1 and (s+t)%2==0:
                    print("Hacked!")
                    return d
e = 80913925630975907286357190125022744799395846719683234341113842760525227640849813045696903138950045040215688057641460047793481444316628227570869150364227916527954282690238712302747490989030548838427203134683640970149881426183909149879773929300104733504373872810629425945474753242948838877004365529566191292489
n = 107252787628390906082192966035810093127477285925557768543493490752323413660034578146490822130048833674323596558460745675443005805857718366184178828995947192223768284762051102948863788408124518665729293409233552762491915219350332353007760219203018548727616356381216301935868788967841774718483453121672076489239
c= 71939185720757860963185416295855941645426314252927726837015875915679761775856499139563893722682774470469279135501876439741003693053004493984797777367689252276035598494617449817038305645332662483995646656189048489898840114749250360999177284680750592181253462178285470159236909889305333883819150107727604747821
d = hack_RSA(e,n)
from Crypto.Util.number import *
m = pow(c,d,n)
print(long_to_bytes(m))
