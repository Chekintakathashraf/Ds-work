# Find length of a string in python

# Python code to demonstrate string length
# using len

str = "geeks"
print(len(str))

print('**************************')

# Python code to demonstrate string length
# using for loop

# Returns length of string
def findLen(str):
	counter = 0
	for i in str:
		counter += 1
	return counter


str = "geeks"
print(findLen(str))

print('**************************')

# Python code to demonstrate string length
# using while loop.

# Returns length of string
def findLen(str):
	counter = 0
	while str[counter:]:
		counter += 1
	return counter

str = "geeks"
print(findLen(str))

print('**************************')

# Python code to demonstrate string length
# using join and count

# Returns length of string
def findLen(str):
	if not str:
		return 0
	else:
		some_random_str = 'py'
		return ((some_random_str).join(str)).count(some_random_str) + 1

str = "geeks"
print(findLen(str))


print('***********************')

# Python code to demonstrate string length
# using reduce

import functools

def findLen(string):
	return functools.reduce(lambda x,y: x+1, string, 0)


# Driver Code
string = 'geeks'
print(findLen(string))


print('***********************')

# Python code to demonstrate string length
# using sum


def findLen(string):
	return sum( 1 for i in string);


# Driver Code
string = 'geeks'
print(findLen(string))


print('***********************')

