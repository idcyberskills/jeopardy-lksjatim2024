import binascii
from ecdsa.curves import NIST256p as curves
from ecdsa.util import  sigdecode_string
from ecdsa import VerifyingKey, SigningKey
from hashlib import sha256
from ecdsa.numbertheory import inverse_mod
from Crypto.Cipher import AES

public_key_pem = '''
-----BEGIN PUBLIC KEY-----

-----END PUBLIC KEY-----
'''.strip()
public_key_ec = VerifyingKey.from_pem(public_key_pem)
n = public_key_ec.curve.order

hash1=''
hash2=''

sig1=''
sig2=''

enc_flag=''

m1 = int(sha256(hash1).hexdigest(), 16)
m2 = int(sha256(hash2).hexdigest(), 16)

(r1, s1) = sigdecode_string(sig1, n)
(r2, s2) = sigdecode_string(sig2, n)
k=((m1 - m2) * inverse_mod(s1 - s2, n)) % n
r_inv = inverse_mod(r1,n)
d_a = ((s1*k - m1) * r_inv) % n

print(d_a)

sk = SigningKey.from_secret_exponent(d_a, curve=curves, hashfunc=sha256)

print(sk.to_pem().decode("utf-8"))

aes_key = d_a.to_bytes(64, byteorder='little')[0:16]

IV = n.to_bytes(64, byteorder='little')[0:16]
cipher = AES.new(aes_key, AES.MODE_EAX, IV)
ctxt = cipher.decrypt(binascii.unhexlify(enc_flag))

print(ctxt)