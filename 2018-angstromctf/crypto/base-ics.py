#!/usr/bin/env python
from Crypto.Util.number import long_to_bytes
enc = [
    '011000010110001101110100011001100111101100110000011011100110010101011111011101000111011100110000010111110110011000110000'
    , '165 162 137 145 151 147 150 164 137 163 151 170 164 63 63'
    , '6e5f7468317274797477305f733178'
    , 'dHlmMHVyX25vX20wcmV9'
]

flag = ''
flag += long_to_bytes(int(enc[0], 2))
flag += ''.join([long_to_bytes(int(i, 8)) for i in enc[1].split(' ')])
flag += enc[2].decode('hex')
flag += enc[3].decode('base64')

print flag