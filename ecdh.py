import random
import time
from Crypto.Util.number import getPrime
# import ecc

def dh(p,generator=65537):
    
    #Alice's choice (private key)
    a = random.randint(2,p-1)

    #Bob's choice (private key)
    b = random.randint(2,p-1)

    while a==b:
        b = random.randint(2,p-1)
    
    alice_pb = pow(generator,a,p)
    bob_pb = pow(generator,b,p)

    dh_share_alice = pow(bob_pb,a,p)
    dh_share_bob = pow(alice_pb,b,p)

    return dh_share_alice,dh_share_bob

def ecdh_key_exchange(a,b,p):

    #Alice's choice (private key)
    na = random.randint(2,p-1)

    #Bob's choice (private key)
    nb = random.randint(2,p-1)

    while na==nb:
        nb = random.randint(2,p-1)

    def pointadd(p1, p2, a, p):
        lamda = 0

        if p1 == p2:
            numerator = (3 * (p1[0]**2) + a) % p
            denominator = (2 * p1[1]) % p
            lamda = (numerator * mod_inverse(denominator, p)) % p
        else:
            numerator = (p2[1] - p1[1]) % p
            denominator = (p2[0] - p1[0]) % p

            if denominator == 0:
                # Point doubling at the point of infinity
                return (0, 0)

            lamda = (numerator * mod_inverse(denominator, p)) % p

        x3 = (lamda**2 - p2[0] - p1[0]) % p
        y3 = (lamda * (p1[0] - x3) - p1[1]) % p

        return (x3, y3)

    def mod_inverse(a, m):
        # Extended Euclidean Algorithm to find modular inverse
        m0, x0, x1 = m, 0, 1
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        return x1 + m0 if x1 < 0 else x1


    def multiply(k, point,a,p):
        """ Multiply a point P with a constant k, using double-and-add. """
        
        result = point
        k-=1
        Q = point

        while k > 0:
            # If the current bit of k is 1, add Q to the result
            if k & 1:
                result = pointadd(result, Q,a,p)

            # Double the point for the next iteration
            Q = pointadd(Q, Q,a,p)

            # Move to the next bit of the scalar
            k >>= 1

        return result
    
    generator = (2,3)
    shared_key_alice = multiply(na,generator,a,p)
    shared_key_bob = multiply(nb,generator,a,p)
    # print(multiply(3,generator,a,p))
    return multiply(nb,shared_key_alice,a,p), multiply(na, shared_key_bob,a,p)


if __name__ == "__main__":
    # 160-bit integer start from 2^159 to 2^160-1
    p = getPrime(160)
    dhP = getPrime(1024)

    print("Ordinary DH protocol:")
    print()

    start_time = time.time()
    dh_share_alice, dh_share_bob = dh(dhP)
    time_dh = time.time() - start_time

    print("Alice's shared secret: ", dh_share_alice)
    print("Bob's shared secret: ", dh_share_bob)
    print("D-H key exchange time: ", time_dh, " seconds")

    print()

    # choose a = 0 and b = 1
    a,b = 0,1

    k = ecdh_key_exchange(a,b,p)
    # print(k)

    start_time = time.time()

    shared_key_alice, shared_key_bob = ecdh_key_exchange(a,b,p)
    time_dh = time.time() - start_time

    print("ECDH process:")
    print()
    print("Shared Key (Alice):", shared_key_alice)
    print("Shared Key (Bob):", shared_key_bob)
    
    print("ECDH key exchange time: ", time_dh, " seconds")

    





