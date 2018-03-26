from Crypto.PublicKey import RSA
from Crypto.Util.number import long_to_bytes, bytes_to_long
from gmpy import invert
pubkey = RSA.importKey(open('public.pem').read())
p, e = pubkey.n, pubkey.e
c = bytes_to_long(open('flag.enc').read().decode('base64'))

d = invert(e, p-1)
m = pow(c, d, p)
flag = long_to_bytes(m)
print flag