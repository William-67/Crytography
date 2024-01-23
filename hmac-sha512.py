import hashlib
import hmac #use for comparing to self-implemented function

def hmac_sha512(key, message):
    block_size = 128  # 128 bytes for SHA-512
    hash_func = hashlib.sha512

    if len(key) > block_size:
        key = hash_func(key).digest()
    elif len(key) < block_size:
        key = key.ljust(block_size, b'\x00')

    ipad = 0x36 #ipad - 00110110 
    inner_key = bytes(x ^ ipad for x in key)
    inner_hash = hash_func(inner_key + message).digest()

    opad = 0x5c #opad - 01011100
    outer_key = bytes(x ^ opad for x in key)
    outer_hash = hash_func(outer_key + inner_hash).digest()

    return outer_hash

# Test the implementation
input_string = "This input string is being used to test my own implementation of HMAC-SHA-512."
secret_key = b"whatever"

# Using the implemented HMAC-SHA-512
my_hmac = hmac_sha512(secret_key, input_string.encode())
print("HMAC-SHA-512 (Implemented):", my_hmac)

# Using the library to confirm the implementation
library_hmac = hmac.new(secret_key, input_string.encode(), hashlib.sha512).digest()
print("HMAC-SHA-512 (Library):", library_hmac)

print("Two hmac are equals: ", my_hmac==library_hmac)