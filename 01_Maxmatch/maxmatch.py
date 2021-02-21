import sys
#dictionary.sort()
#dictionary.reverse()

def maxmatch(sentence, dictionary):
        #dictionary = a dictionary containing your vocabulary
        #return dictionary value for sentence
        if sentence == '':
                return []
        #for variable i in the range from the start of the sentence to the end of the sentence
        for i in range(0, len(sentence)):
                #the first word is the word located between 0 and -i
                firstword = sentence[0:-i]
                # the remainder is everything after
                remainder = sentence[-i:]
                #if there is a match between the first word and a dictionary entry
                if firstword in dictionary:
                        #return the first word and the maxmatch of the rest of the sentence and the dictionary
                        return [firstword] + maxmatch(remainder, dictionary)
        #Otherwise the first word is located at 0
        firstword = sentence[0]
        #and the remainder is everything after 1
        remainder = sentence[1:]
        #return the first word plus the remainder's maxmatch
        return ([firstword] + maxmatch(remainder, dictionary))

dictionary = [line.strip() for line in open("extracted_japanese.txt").readlines()]
fd = open(sys.argv[1])
line = fd.readline()
while line != '':
        #print out the maxmatch tokenised line
        print(maxmatch(dictionary, line.strip('\n')))
        #read a line from the file
        line = fd.readline()
#Some error with lists? or possibly I need a dict file?
