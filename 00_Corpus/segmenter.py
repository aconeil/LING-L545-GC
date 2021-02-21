import sys
import re

line = sys.stdin.readline()

#while the line is not empty
while line != '':
	#split the entries on the line at the space
	for token in line.split(' '):
		#if the token is new line
		if token == '\n':
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
		#if the last code of the token is a quote mark
		if token[-1] in '"':
			if re.findall('\."', token):
				sys.stdout.write(token + '\n')
			else:
				sys.stdout.write(token + ' ')
		#if the last character of the token is a period
		elif token[-1] in '.':
#			if the token is in the list
			if token in ['Dr.','etc.','i.e.', 'e.g.', 'St.', '...']:
				sys.stdout.write(token + ' ')
			#if the token uses a period following one or more numbers
			elif re.findall('[0-9]+\.[0-9]+\.', token):
			#write out the token with a space following it
				sys.stdout.write(token + ' ')
			#if the token is a capital letter followed by a period
	#		elif re.findall('[A-Z]+\.',token):
	#			sys.stdout.write(token + '\n')
			elif re.findall('[A-Z]\.',token):
				if re.findall('[A-Z][A-Z]+\.', token):
					sys.stdout.write(token + '\n')
				else:
					sys.stdout.write(token + ' ')
		#otherwise write it out with newline following it
			else:
				sys.stdout.write(token + '\n')
	#print out the tokens with space between if last charcter in token is not !?.
		else:
			sys.stdout.write(token + ' ')
	line = sys.stdin.readline()
