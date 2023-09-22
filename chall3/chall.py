from Crypto.Util.number import getPrime
from secret import FLAG
import random

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
    global N, e
    p = getPrime(512)
    q = getPrime(512)
    N = p * q
    e = 0x10001
    print(f"public key = {(N, e)}")

def encrypt(msg: bytes, buggy=False):
    m = bytes2int(msg)

    if buggy:
        c = pow(m, e ^ 8, N)
    else:
        c = pow(m, e, N)

    print(f"ciphertext = {c}")

def bytes2int(msg):
    return int.from_bytes(msg, "big")
    
if __name__ == "__main__":
    main()