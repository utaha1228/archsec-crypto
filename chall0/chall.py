from Crypto.Util.number import getPrime
from secret import FLAG

def main():
	m = bytes2int(FLAG)
	p = getPrime(64)
	q = getPrime(64)
	N = p * q
	e = 0x10001
	c = pow(m, e, N)

	print(f"Public key: {(N, e)}")
	print(f"Ciphertext: {c}")

def int2bytes(n):
	length = (n.bit_length() + 7) // 8
	return n.to_bytes(length, "big")

def bytes2int(s):
	return int.from_bytes(s, "big")

if __name__ == "__main__":
	main()