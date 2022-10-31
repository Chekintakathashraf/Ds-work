# words which are greater than given length k

# Python program to find all string
# which are greater than given length k

# function find string greater than length k
def string_k(k, str):
	
	# create the empty string
	string = []
	
	# split the string where space is comes
	text = str.split(" ")
	
	# iterate the loop till every substring
	for x in text:
		
		# if length of current sub string
		# is greater than k then
		if len(x) > k:
			
			# append this sub string in
			# string list
			string.append(x)
			
	# return string list
	return string


# Driver Program	
k = 3
str ="geek for geeks"
print(string_k(k, str))


print('**********')

'''Method: Using list comprehension'''

sentence = "hello geeks for geeks is computer science portal"
length = 4
print([word for word in sentence.split() if len(word) > length])


print('******************')

'''Method: Using lambda function 

'''

n="hello geeks for geeks is computer science portal"; l=4
s=n.split(" ")
l=list(filter(lambda x: (len(x)>l),s))
print(l)


print('******************')

'''Method: Using the enumerate function '''

sentence = "hello geeks for geeks is computer science portal"
length = 4
s=sentence.split()
print([a for i,a in enumerate(s) if len(a) > length])
