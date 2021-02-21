import sys

line = sys.stdin.readline()

#while the line is not empty
while line != '':
	#split the entries on the line at the space
	for token in line.split(' '):
		#if the token is new line
		if token == '\n':
			#print the new line
			print(token)
		#strip all tokens of newline
		token = token.strip()
		#if the token is empty
		if token == '':
			#skip it and continue
			continue
		#if the last character of the sentence is ! or ? add newline after it
		if token[-1] in '!?':
			sys.stdout.write(token + '\n')
		#if the last character of the period is a period
		elif token[-1] in '.':
#			if the token is in the list
			if token in ['Dr.','etc.','i.e.', 'e.g.', 'St.', '...']:
			#write out the token with a space following it
				sys.stdout.write(token + ' ')
			#add new line to all tokens following a period
			#otherwise write it our with newline following it
			else:
				sys.stdout.write(token + '\n')
		#print out the tokens with space between if last charcter in token is not !?.
		else:
			sys.stdout.write(token + ' ')
	line = sys.stdin.readline()
