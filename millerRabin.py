import random

# d*2^r = n-1
def miller_rabin(n, t=6):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    # Write n as 2^r * d + 1
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # start testing 
    for _ in range(t):

        a = random.randint(2, n - 2)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:

            continue

        for _ in range(r - 1):

            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True  # n is probably prime

if __name__ == "__main__":
    while True:

        # candidate = random.getrandbits(15)
        
        #15 bit integer start from 16384(which is 2^14) to 32767(2^15-1)
        randomPrime = random.randint(16384,32767)

        #make sure it is always odd
        if randomPrime % 2 == 0:
            randomPrime +=1

        if miller_rabin(randomPrime,6):
            print("The 15-bit probably prime number is: ", randomPrime)
            break

        

