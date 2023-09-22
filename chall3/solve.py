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

m8 = c2 * pow(c1, -1, N) % N
flag = c1 * pow(m8, -65536 // 8, N) % N
print(bytes.fromhex(hex(flag)[2:]))