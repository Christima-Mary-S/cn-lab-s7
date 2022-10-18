code=input("Enter the code word: ")
compressed=code.split(" ")
map_object=map(int,compressed)
compressed=list(map_object)
dictionary={}
dict_size=1
n=int(input("Enter the number of inputs in the basic dictionary: "))
print("Enter the basic dictionary: ")
for i in range(n):
	c=input("Enter the character: ")
	dictionary[dict_size]=c
	dict_size+=1
result = ""
w = dictionary[compressed.pop(0)]
result+=w
for k in compressed:
	if k in dictionary:
		entry = dictionary[k]
	elif k == dict_size:
		entry = w + w[0]
	else:
		raise ValueError('Bad compressed k: %s' % k)
	result+=entry
	dictionary[dict_size] = w + entry[0]
	dict_size += 1
	w = entry
print(result)

#OUTPUT
#Enter the code word: 1 2 3 5 4 
#Enter the number of inputs in the basic dictionary: 2
#Enter the basic dictionary: 
#Enter the character: a
#Enter the character: b
#ababababa
