from itertools import permutations
from itertools import cycle

def encrypt():
	msg = "t0r0nt0_ch4ll{X0r_0p3R4t10N_34Zy}"
	key = "vxspmlq"

	encrypted = ""
	for (a, b) in zip(msg, cycle(key)):
		encrypted += "".join(chr(ord(a) ^ ord(b)))

	encrypted = encrypted.encode("utf-8").hex()
	print(encrypted)

def decrypt():
	encrypted_msg = input("Encrypted: ")
	key = "73716C7076786D"
	permutations_key = permutations([str(x) for x in bytes.fromhex(key).decode()])

	for i in permutations_key:
		for (a, b) in zip(bytearray.fromhex(encrypted_msg).decode(), cycle(i)):
			print(chr(ord(a) ^ ord(b)), end='')
		print("\n")

encrypt()
decrypt()
