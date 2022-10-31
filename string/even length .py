# Python program to print even length words in a string



#input string
n="This is a python language"
#splitting the words in a given string
s=n.split(" ")
for i in s:
#checking the length of words
    if len(i)%2==0:
        print(i)

# this code is contributed by gangarajula laxmi

print('*****************')

# Python3 program to print
# even length words in a string

def printWords(s):
	
	# split the string
	s = s.split(' ')
	
	# iterate in words of string
	for word in s:
		
		# if length is even
		if len(word)%2==0:
			print(word)


# Driver Code
s = "i am muskan"
printWords(s)


print('*******************')

# Python code
# To print even length words in string

#input string
n="geeks for geek"
#splitting the words in a given string
s=n.split(" ")
l=list(filter(lambda x: (len(x)%2==0),s))
print(l)


print('****************')

# python code to print even length words

n="geeks for geek"
s=n.split(" ")
print([x for x in s if len(x)%2==0])


print('***************')

# python code to print even length words

n="geeks for geek"
s=n.split(" ")
print([x for i,x in enumerate(s) if len(x)%2==0])
