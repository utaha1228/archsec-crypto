from pwn import *
import math

conn = process(["python3", "chall.py"])

conn.recvuntil(b"public key = ")
N, e = eval(conn.recvline().decode("ascii"))

conn.sendline(b"1")
conn.recvuntil(b"ciphertext = ")
c1 = int(conn.recvline().decode("ascii"))

conn.sendline(b"2")
conn.recvuntil(b"ciphertext = ")
c2 = int(conn.recvline().decode("ascii"))

p = math.gcd(N, c1 - c2)
q = N // p
d = pow(e, -1, (p - 1) * (q - 1))
flag = pow(c1, d, N)

print(bytes.fromhex(hex(flag)[2:]))