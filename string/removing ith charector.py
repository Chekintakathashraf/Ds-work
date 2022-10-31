# removing i-th character from a string

# Python3 program for removing i-th
# indexed character from a string

# Removes character at index i
def remove(string, i):

	# Characters before the i-th indexed
	# is stored in a variable a
	a = string[ : i]
	
	# Characters after the nth indexed
	# is stored in a variable b
	b = string[i + 1: ]
	
	# Returning string after removing
	# nth indexed character.
	return a + b
	
# Driver Code
if __name__ == '__main__':
	
	string = "geeksFORgeeks"
	
	# Remove nth index element
	i = 5
	
	# Print the new string
	print(remove(string, i))


print('************************')

'''Approach 2 : The idea is to use string replace in Python'''

# Python3 program for removing i-th
# indexed character from a string

# Removes character at index i
def remove(string, i):

	for j in range(len(string)):
		if j == i:
			string = string.replace(string[i], "", 1)
	return string
	
# Driver Code
if __name__ == '__main__':
	
	string = "geeksFORgeeks"
	
	# Remove nth index element
	i = 5
	
	# Print the new string
	print(remove(string, i))
