# Odd Frequency Characters

'''Method #1 : Using defaultdict() + list comprehension + loop'''

# Python3 code to demonstrate working of
# Odd Frequency Characters
# Using list comprehension + defaultdict()
from collections import defaultdict

# helper_function
def hlper_fnc(test_str):
	cntr = defaultdict(int)
	for ele in test_str:
		cntr[ele] += 1
	return [val for val, chr in cntr.items() if chr % 2 != 0]

# initializing string
test_str = 'geekforgeeks is best for geeks'

# printing original string
print("The original string is : " + str(test_str))

# Odd Frequency Characters
# Using list comprehension + defaultdict()
res = hlper_fnc(test_str)

# printing result
print("The Odd Frequency Characters are :" + str(res))

print('**********************8')

'''Method #2 : Using list comprehension + Counter() '''

# Python3 code to demonstrate working of
# Odd Frequency Characters
# Using list comprehension + Counter()
from collections import Counter

# initializing string
test_str = 'geekforgeeks is best for geeks'

# printing original string
print("The original string is : " + str(test_str))

# Odd Frequency Characters
# Using list comprehension + Counter()
res = [ chr for chr, count in Counter(test_str).items() if count & 1 ]

# printing result
print("The Odd Frequency Characters are : " + str(res))

print('*****************************')

'''Method #3 : Using count() method.'''

# Python3 code to demonstrate working of
# Odd Frequency Characters


# initializing string
test_str = 'geekforgeeks is best for geeks'

# printing original string
print("The original string is : " + str(test_str))

# Odd Frequency Characters
x=set(test_str)
res=[]
for i in x:
	if(test_str.count(i)%2!=0):
		res.append(i)
# printing result
print("The Odd Frequency Characters are : " + str(res))
