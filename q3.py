import sympy
import hashlib
import random

def generate_prime():

    q = sympy.randprime(2**159, 2**160)
    
    random_number = random.randrange(2**(864), 2**(865))

    p = q * random_number + 1

    while (not sympy.isprime(p)):
    	random_number = random.randrange(2**(864), 2**(865))
    	p = q * random_number + 1

    return p,q,random_number

def create_generator(p,q,random_number):

	h = random.randint(2,p-2)
	g = pow(h,random_number, p)
	return g

def user_key(g,p,q):

	x = random.randrange(2,q-1)
	y = pow(g,x,p)
	return x,y

def signing(m,p,q,g,x,k=5):

	m = str(m)
	r = pow(g,k,p) % q

	hash_value = int(hashlib.sha1(m.encode()).hexdigest(),16)

	s = (pow(k,-1,q) * (hash_value + x * r)) % q

	return r,s

def verify(m,r,s,p,q,g,y):

	m = str(m)
	hash_value = int(hashlib.sha1(m.encode()).hexdigest(),16)

	w = pow(s,-1,q)
	u1 = (hash_value * w) % q
	u2 = (r * w) % q
	output = ((pow(g,u1,p) * pow(y,u2,p)) % p) % q

	return output


p, q, random_number = generate_prime()
g = create_generator(p, q, random_number)
x, y = user_key(g, p, q)
print("x (private key):", x)

# First signing
m1 = 8161474912583
r1, s1 = signing(m1, p, q, g, x)

m2 = 58234682955761
r2, s2 = signing(m2, p, q, g, x)

# Verification
output1 = verify(m1, r1, s1, p, q, g, y)
output2 = verify(m2, r2, s2, p, q, g, y)

print("Verify the first signature is:", s1)
print("Verify the second signature is:", s2)

print()
print("On attacker side: ")

h1 = int(hashlib.sha1(str(m1).encode()).hexdigest(),16)
h2 = int(hashlib.sha1(str(m2).encode()).hexdigest(),16)

numerator = (h1-h2) % q
denominator = (s1-s2) % q

k = (numerator * pow(denominator,-1,q)) % q

attackerX = ((k*s1 - h1) * pow(r1,-1,q)) % q

print("k is (H(m1)-H(m2))/(s1-s2): ", k)
print("private key x is (k*s1 - H(m1)) * r^-1 mod q: ",attackerX)