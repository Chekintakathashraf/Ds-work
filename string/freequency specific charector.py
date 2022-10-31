# Specific Characters Frequency in String List

'''Method #1 : Using join() + Counter()'''

# Python3 code to demonstrate working of
# Specific Characters Frequency in String List
# Using join() + Counter()
from collections import Counter

# initializing lists
test_list = ["geeksforgeeks is best for geeks"]

# printing original list
print("The original list : " + str(test_list))

# char list
chr_list = ['e', 'b', 'g']

# dict comprehension to retrieve on certain Frequencies
res = {key:val for key, val in dict(Counter("".join(test_list))).items() if key in chr_list}
	
# printing result
print("Specific Characters Frequencies : " + str(res))


print('*************************')

'''Method #2 : Using chain.from_iterable() + Counter() + dictionary comprehension'''

# Python3 code to demonstrate working of
# Specific Characters Frequency in String List
# Using chain.from_iterable() + Counter() + dictionary comprehension
from collections import Counter
from itertools import chain

# initializing lists
test_list = ["geeksforgeeks is best for geeks"]

# printing original list
print("The original list : " + str(test_list))

# char list
chr_list = ['e', 'b', 'g']

# dict comprehension to retrieve on certain Frequencies
# from_iterable to flatten / join
res = {key:val for key, val in dict(Counter(chain.from_iterable(test_list))).items() if key in chr_list}
	
# printing result
print("Specific Characters Frequencies : " + str(res))


print('******************8')

'''Method #3:Using count() method.count() method returns the number of times a particular element occurs in a sequence.'''

# Python3 code to demonstrate working of
# Specific Characters Frequency in String List

# initializing lists
test_list = ["geeksforgeeks is best for geeks"]

# printing original list
print("The original list : " + str(test_list))

# char list
chr_list = ['e', 'b', 'g']

d=dict()
for i in chr_list:
	d[i]=test_list[0].count(i)
res=d
	
# printing result
print("Specific Characters Frequencies : " + str(res))
