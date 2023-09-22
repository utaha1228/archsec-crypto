from Crypto.Util.number import getPrime
import random
from secret import FLAG

def main():
    init()
    while True:
        option = int(input())
        if option == 1:
            encrypt(FLAG, buggy=False)
        elif option == 2:
            encrypt(FLAG, buggy=True)
        else:
            exit(0)

def init():
    global p, q, e
    p = getPrime(512)
    q = getPrime(512)
    e = 0x10001

def encrypt(msg: bytes, buggy=False):
    if buggy:
        bit_idx = random.randrange(0, 512)
        N = p * (q ^ (1 << bit_idx))
    else:
        N = p * q

    m = bytes2int(msg)
    c = pow(m, e, N)
    print(f"public key = {(N, e)}")
    print(f"ciphertext = {c}")

def bytes2int(msg):
    return int.from_bytes(msg, "big")
    
if __name__ == "__main__":
    main()