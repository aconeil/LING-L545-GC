import sys, re
vowels = 'AEIOUaeiouéɔɛƆụāīăịəæë'
vocab = {}
line = sys.stdin.readline()
while line:
	for token in line.strip().split(' '):
		patron = ''
		for c in token:
			if c in vowels:
				patron += '#'
			else:
				patron += c
		if patron not in vocab:
			vocab[patron] = []
		vocab[patron].append(token)

	line = sys.stdin.readline()
for patron in vocab:
	print(patron, list(set(vocab[patron])))

