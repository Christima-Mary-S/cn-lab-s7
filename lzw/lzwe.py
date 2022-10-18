import sys
from sys import argv
from struct import *
uncompressed=input("Enter the string: ")
dict_size = 1
char_seen = []
dictionary={}
for char in uncompressed:
	if char not in char_seen:
		char_seen.append(char)
string=''.join(char_seen)
for i in string:
	dictionary[i] = dict_size
	dict_size+=1
w = ""
result = []
for c in uncompressed:
	wc = w + c
	if wc in dictionary:
		w = wc
	else:
		result.append(dictionary[w])
		dictionary[wc] = dict_size
		dict_size += 1
		w = c
# Output the code for w.
if w:
	result.append(dictionary[w])
print(result)

#OUTPUT
#Enter the string: ababababa
#[1, 2, 3, 5, 4]

