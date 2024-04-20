from ecdsa import SigningKey
from ecdsa.curves import NIST256p as curves
import random
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import binascii
from hashlib import sha256
from ecdsa.util import sigencode_string
	
def get_flag():
    FLAG = os.environ.get("FLAG")
    FLAG = pad(FLAG.encode(), 16)
    return FLAG

signer = SigningKey.generate(curve=curves, hashfunc=sha256)
private_key = signer.privkey
public_key = signer.verifying_key

nonce = random.randrange(1, 2**127)

hash1 = os.urandom(16)
hash2 = os.urandom(16)

sig1 = signer.sign(hash1, hashfunc=sha256, sigencode=sigencode_string, k=nonce)
sig2 = signer.sign(hash2, hashfunc=sha256, sigencode=sigencode_string, k=nonce)

print(public_key.to_pem().decode("utf-8"))
print("s1: " + str(sig1))
print("s2: " + str(sig2))
print("")
print("hashes:")
print(hash1)
print(hash2)
print("")

aes_key = private_key.secret_multiplier.to_bytes(64, byteorder='little')[0:16]
IV = private_key.order.to_bytes(64, byteorder='little')[0:16]

ptxt =  get_flag()
cipher = AES.new(aes_key, AES.MODE_EAX, IV)
ctxt = cipher.encrypt(ptxt)

print("Encrypted Flag:")
print(binascii.hexlify(ctxt))
