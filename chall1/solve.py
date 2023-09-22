from pwn import *
import math

conn = process(["python3", "chall.py"])

conn.sendline(b"1")
conn.recvuntil(b"public key = ")
N1, e = eval(conn.recvline().decode("ascii"))
conn.recvuntil(b"ciphertext = ")
c1 = int(conn.recvline().decode("ascii"))

conn.sendline(b"2")
conn.recvuntil(b"public key = ")
N2, e = eval(conn.recvline().decode("ascii"))
conn.recvuntil(b"ciphertext = ")
c2 = int(conn.recvline().decode("ascii"))

p = math.gcd(N1, N2)
q = N1 // p
d = pow(e, -1, (p - 1) * (q - 1))
flag = pow(c1, d, N1)

print(bytes.fromhex(hex(flag)[2:]))