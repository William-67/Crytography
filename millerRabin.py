import random

# millerRabin.py
# Description: This file perform miller-rabin test for large prime number and generate it by specifying size of the prime
# Theory: for any positive odd integer n > 2, n can be express as
#         n-1 = 2^r * d with k > 0 and d is odd
#         consider an integer a, which is relatively prime to n
#         n is said to be strong probable prime to base a if one of these holds:
#         a^d = 1 (mod n) or a^(2^(s) * d) = n-1 (mod n) for 0 <= s < r


def miller_rabin(n, t=6):
    '''(int,int) -> boolean
        n: An large integer for primality test
        t: Confidence of the test
        The algorithm will run t times with different base number "a"
        return false if the number fail the condition from theory
        return true if the number pass the test with confidence of "t"
    '''

    #Base case test for primality 
    #if the number is even, return directly "is not prime"
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    # Write n as 2^r * d + 1
    # find r and d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # start testing 
    for _ in range(t):

        a = random.randint(2, n - 2)
        x = pow(a, d, n) # x = a^d (mod n)

        if x == 1 or x == n - 1:
            continue
            
        for _ in range(r - 1):

            x = pow(x, 2, n) # (a^d)^(2^s) for s from 0 to r-1
            if x == n - 1:

                break
        else:

            return False

    return True  # n is probably a prime

if __name__ == "__main__":

    #This is a generator for generating 15 bit prime number
    while True:

        # candidate = random.getrandbits(15)
        
        #15 bit integer start from 16384(which is 2^14) to 32767(which is 2^15-1)
        randomPrime = random.randint(16384,32767)

        #make sure it is always odd
        if randomPrime % 2 == 0:
            randomPrime +=1

        if miller_rabin(randomPrime,6):
            print("The 15-bit probably prime number is: ", randomPrime)
            break

        

