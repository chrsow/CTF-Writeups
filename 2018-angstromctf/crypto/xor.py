#!/usr/bin/env python3
import codecs
# def or()
c = codecs.decode('fbf9eefce1f2f5eaffc5e3f5efc5efe9fffec5fbc5e9f9e8f3eaeee7','hex')
k = chr(c[0]^ord('a'))
flag = ''
for i in c:
    flag += chr(i^ord(k))
print(flag)