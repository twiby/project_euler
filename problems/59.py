import numpy as np

def decrypt(message, key):
	return [chr(i) for i in message ^ key]
	ret = []
	key_idx = 0
	for c in message:
		ret.append(chr(c ^ key[key_idx]))
		key_idx = (key_idx + 1) % len(key)
	return ret

def main():
	with open("./data/p059_cipher.txt","r") as f:
		cipher = np.array([int(c) for c in next(f).split(",")])

	KEY = [0,0,0]

	max_nb_e = 0
	for c1 in range(ord("a"), ord("z")+1):
		key = np.resize([c1,0,0], len(cipher))
		decrypted = np.array(decrypt(cipher, key))
		nb_e = np.sum(decrypted == "e")
		if nb_e > max_nb_e:
			max_nb_e = nb_e
			KEY[0] = c1
	max_nb_e = 0
	for c2 in range(ord("a"), ord("z")+1):
		key = np.resize([0,c2,0], len(cipher))
		decrypted = np.array(decrypt(cipher, key))
		nb_e = np.sum(decrypted == "e")
		if nb_e > max_nb_e:
			max_nb_e = nb_e
			KEY[1] = c2
	max_nb_e = 0
	for c3 in range(ord("a"), ord("z")+1):
		key = np.resize([0,0,c3], len(cipher))
		decrypted = np.array(decrypt(cipher, key))
		nb_e = np.sum(decrypted == "e")
		if nb_e > max_nb_e:
			max_nb_e = nb_e
			KEY[2] = c3

	KEY = np.resize(KEY, len(cipher))
	return sum([ord(c) for c in decrypt(cipher, KEY)])

if __name__ == "__main__":
	print(main())