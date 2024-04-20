from pwn import *

r = remote("localhost",10001)
r.sendline("G")
r.recvuntil("| encrypt(flag) = ")
s1 =binascii.unhexlify(r.recvline()[:-1]) 
s2 = "A"*len(s1)
r.sendline("T")
r.sendline(s2)
r.recvuntil("| enc = ")
s3 = binascii.unhexlify( r.recvline()[:-1]) [:len(s1)]
print(xor(xor(s1,s2),s3))
