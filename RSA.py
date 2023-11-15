import time
import elgamal
from Crypto.Util.number import getPrime
# import millerRabin

def encryption(m,e,n):

    ciphertext = pow(m,e,n)

    return ciphertext

def normal_decryption(ciphertext,d,n):

    plaintext = pow(ciphertext,d,n)

    return plaintext

def crt_decryption(ciphertext,d,p,q):

    dp = d % (p-1)
    dq = d % (q-1)
    qinv = elgamal.multiplicative_inverse(q,p) # q^-1 mod p
    # qinv = (qinv * q) % p 

    mp = pow(ciphertext,dp,p)
    mq = pow(ciphertext,dq,q)

    h = (qinv * (mp-mq)) % p
    plaintext = mq + h * q

    return plaintext

if __name__ == "__main__":

    p = getPrime(1024)
    q = getPrime(1024)

    # print(p,q)
    n = p * q
    phi = (p-1) * (q-1)

    #global variable
    e = 65537
    m = 476921883457909

    d = elgamal.multiplicative_inverse(e, phi)
    # # print(d)
    # publicKey = (e,n)
    # privateKey = d
    
    ciphertext = encryption(m,e,n)

    start = time.time()
    normal_decrypt_m = normal_decryption(ciphertext,d,n)
    normal_de_time = time.time() - start

    print("Decrypted message without CRT: ", normal_decrypt_m)
    print("Decryption time without CRT:", normal_de_time," seconds")
    print()

    start = time.time()
    crt_decrypt_m = crt_decryption(ciphertext,d,p,q)
    crt_de_time = time.time() - start

    print("Decrypted message with CRT: ", crt_decrypt_m)
    print("Decryption time with CRT:", crt_de_time," seconds")
