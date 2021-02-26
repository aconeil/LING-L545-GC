import sys

def maxmatch(sentence, dictionary):
        #dictionary = a dictionary containing your vocabulary
        #if sentence is not empty return a list
        if sentence == '':
                return []
        #for a variable in the range from the start of the sentence to the maximum length of the sentence
        for i in range(0, len(sentence)):
                #the first word is the word located between the start of the sentence and the value i from the end of the sentence
                firstword = sentence[0:-i]
#               print(firstword)
                # the remainder is everything after
                remainder = sentence[-i:]
                #if there is a match between the first word and a dictionary entry
                if firstword in dictionary:
                       #return the first word and the maxmatch of the rest of the sentence and the dictionary
                        return [firstword] + maxmatch(remainder, dictionary)
                #Otherwise the first word is the first character
        firstword = sentence[0]
                #and the remainder is one and everything after it
        remainder = sentence[1:]
                #return the first word plus the maxmatch for the remainder
        return [firstword] + maxmatch(remainder, dictionary)

#the dictionary is a list of the text in the extracted japanese text file that is stripped of newline
dictionary = [line.strip() for line in open("ja-extracted.txt").readlines()]
#open the file from the file on the command line:
fd = open(sys.argv[1])
line = fd.readline()

#line = sys.stdin.readline()
#while the line is not an empty string
while line != '':
        #print out the maxmatch tokenised line
        print(' '.join(maxmatch(line.strip('\n'),dictionary)))
        line = fd.readline()
