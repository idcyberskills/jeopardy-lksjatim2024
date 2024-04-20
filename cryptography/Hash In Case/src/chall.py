#!/usr/bin/env python3

from Cryptodome.Cipher import AES
import os, time, sys, random
from flag import flag

p = b'LKSEnjoyer2024!!'

def s_m():
	return sys.stdin.readline().strip()

def enc(m, p, iv):
	header = 'EPOCH:' + str(int(time.time()))
	m = header + "\n" + m + '=' * (15 - len(m) % 16)
	aes = AES.new(p, AES.MODE_GCM, iv)
	enc = aes.encrypt_and_digest(m.encode('utf-8'))[0]
	return enc

def pr(*args):
	s = " ".join(map(str, args))
	sys.stdout.write(s + "\n")
	sys.stdout.flush()

def main():
	pad = "+"
	pr(pad*51)
	pr(pad, "  Hi LKS Enjoyer!!                             ", pad)
	pr(pad, "  can you decrypt the encrypted message below? ", pad)
	pr(pad*51)

	iv = os.urandom(random.randint(1, 11))
	flag_enc = enc(flag, p, iv)

	while True:
		pr("| Options: \n|\t[F] Get the encrypted flag \n|\t[E]ncrypt message \n|\t[Q]uit")
		opt = s_m().lower()
		if opt == 'f':
			pr(f'| encrypt(flag) = {flag_enc.hex()}')
		elif opt == 'E':
			pr("| Enter message to be encrypted: ")
			msg_inp = s_m()
			enc = enc(msg_inp, p, iv).hex()
			pr(f'| enc = {enc}')
		elif opt == 'q':
			pr("Quitting ...")
			quit()
		else:
			pr("| Enter Correct Option! ")

if __name__ == '__main__':
	main()