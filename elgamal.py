import random

def keyGeneration():

	print("Key generation process: ")
	print("Select private Xa from (1,q-1)")
	Xa =  random.randint(2,q-2)
	print("Xa is: ", str(Xa))

	Ya = (a**Xa) % q
	print("Calculate Ya: ", Ya)
	print("public and private keys are: {", str(q),str(a),str(Ya), "} {", str(Xa), "}")
	print()

	return (q,a,Ya), Xa

def encryption(m1,k):

	public, private = keyGeneration()
	print("Encryption process:")

	Xa = private
	Ya = public[2]

	K1 = (Ya**k) % q

	print("Using public key to generate one time key, K is: ", K1)

	c1 = (a**k) % q
	c2 = (K1 * m1) % q

	print("ciphertext c1 nad c2 are: ", str(c1)," ", str(c2))
	print()
	return (c1,c2,Xa)

def decryption(ciphertext):

	print("Hellman decryption process:")
	c1, c2, Xa = ciphertext[0], ciphertext[1], ciphertext[2]
	K = (c1 ** Xa) % q
	print("recover K from c1 using private key: ", K)

	m2 = (c2 * multiplicative_inverse(K,q)) % q
	print("plaintext is: ", m2)

def ELGdecryption(ciphertext):

	print("Elgamal decryption process:")
	c1, c2, Xa = ciphertext[0], ciphertext[1], ciphertext[2]

	m2 = (c2 * (multiplicative_inverse(c1,q))**Xa) % q
	print("plaintext is: ", m2)


def multiplicative_inverse(k,q):
	
	# k * (d-1) = 1 mod q
	flag = False
	if k>q:
		k,q = q,k
		flag = True
	a,b = k,q
	s1,s2 = 1, 0
	t1,t2 = 0, 1

	while True:
		g = q // k
		r = q % k 
		s = s1 - g * s2
		t = t1 - g * t2
		# print(q,k,s2,t2)
		if r == 0:
			break

		s1,s2 = s2,s
		t1,t2 = t2,t
		q, k = k, r
	# print(t2)
	if flag:
			return (s2 + b) % b
	else:
			return (t2 + b) % b

if __name__ == "__main__":

	#Global public elements

	q = 89
	a = 13 # this is alpha not a 

	#encryption key
	k = 43

	ciphertext = encryption(62,k)
	decryption(ciphertext)
	ELGdecryption(ciphertext)