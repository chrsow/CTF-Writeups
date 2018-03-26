enc = open('flag.png.crypt').read()
# 1st PNG byte
head = '89'.decode('hex')

def xor(a,b):
    return ''.join([chr(ord(x)^ord(y)) for x,y in zip(a,b)])

k = xor(enc[0],head)

dec = ''
for i in enc:
    dec += xor(k, i)

with open('flag.png', 'w') as f:
    f.write(dec)
    f.close()
    
# Flag{Hopefully_headers_are_constants}