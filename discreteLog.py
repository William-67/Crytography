import sympy
import hashlib
import random


def find_log(g,p,y):

	x = 1
	while pow(g,x,p) != y:
		x+=1

	return x

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

(p, q, g) = (103687, 1571, 21947)
y = 31377
samanPK = find_log(g,p,y)

print(samanPK)

k,m = 1105,510
r,s = signing(m,p,q,g,samanPK,k)

print("r : ", r)
print("s : ", s)