from Crypto.Util.number import *

N, e = (169473153577992185622019168111257898051, 65537)
c = 116122678835514589821268549116909564580
p = 10362612693694928143
q = N // p

d = pow(e, -1, (p - 1) * (q - 1))
m = pow(c, d, N)
print(long_to_bytes(m))

