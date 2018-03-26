#!/usr/bin/env python
import struct
from gmpy import invert

enc = open('flag.png.enc').read()
enc += '\x00' * (-len(enc) % 4)
print len(enc)
enc = [enc[i:i+4] for i in range(0, len(enc), 4)]

# PNG head, trail data format
x1 = 0x89504E47 ^ struct.unpack('>I', enc[0])[0]
x2 = 0x0D0A1A0A ^ struct.unpack('>I', enc[1])[0]
x3 = 0x0000000D ^ struct.unpack('>I', enc[2])[0]
x4 = 0x49484452 ^ struct.unpack('>I', enc[3])[0]

m = pow(2, 32)
c = ( int(invert(x1 - x3, m)) * ( ((x1*x4) % m) - ((x3*x2) % m) ) % m ) % m
a = ( int(invert(x3, m)) * ((x4 - c) % m)) % m
def lcg(m, a, c, x):
	return (a*x + c) % m
    
x = x1
dec = ''
for i in range(len(enc)):
    dec += struct.pack('>I', x ^ struct.unpack('>I', enc[i])[0])
    # x = dlcg(x)
    x = lcg(m, a, c, x)
    
with open('flag.png', 'w') as f:
	f.write(dec)
	f.close()
