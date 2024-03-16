from PIL import Image
from Crypto.Util.number import *
import os, numpy
duck = Image.open("LKS_challenge.png",'r')
w, h = duck.size
pixel_of_dusts = list(duck.getdata())
counter = 0
data = ""
for pix in pixel_of_dusts:
	pix = list(pix)
	if counter < 85 * 8:
		data += chr(pix[2])
		counter += 1
	elif counter == 85:
		break
print(b"FLAG = "+long_to_bytes(int(data,2)))
