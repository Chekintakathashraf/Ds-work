# Permutation of a given string using inbuilt function

# Function to find permutations of a given string
from itertools import permutations

def allPermutations(str):
	
	# Get all permutations of string 'ABC'
	permList = permutations(str)

	# print all permutations
	for perm in list(permList):
		print (''.join(perm))
	
# Driver program
if __name__ == "__main__":
	str = 'ABC'
	allPermutations(str)


print('*******************')

from itertools import permutations
import string

s = "GEEK"
a = string.ascii_letters
p = permutations(s)

# Create a dictionary
d = []
for i in list(p):

	# Print only if not in dictionary
	if (i not in d):
		d.append(i)
		print(''.join(i))
