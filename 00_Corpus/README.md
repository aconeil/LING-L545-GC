# README for Segmentation 
### This code for segmenting texts in Yoruba has been built to correctly segement text with the following:
* Sentences ending in a period, exclamation, or question mark
* Lists starting with numerals
* Initials of people
* Numbers formatted using periods
* Dates formatted using periods
### The segmenting code is mostly accurate on the held-out portion of the text, with the exception of extra new lines. However, in the original text files, new line has been to end sentences, so removing newline completley creates problems for the intial segmentation of the text. In terms of incorrect sentences, only the final sentence appears to be segmented incorrectly. It seems in the case of this sentence it would be best to segement the text in <> as separate sentences. 
