# Python – Avoid Spaces in string length

# Python3 code to demonstrate working of
# Avoid Spaces in Characters Frequency
# Using isspace() + sum()

# initializing string
test_str = 'geeksforgeeks 33 is best'

# printing original string
print("The original string is : " + str(test_str))

# isspace() checks for space
# sum checks count
res = sum(not chr.isspace() for chr in test_str)
	
# printing result
print("The Characters Frequency avoiding spaces : " + str(res))


print('***********************')

# Python3 code to demonstrate working of
# Avoid Spaces in Characters Frequency
# Using sum() + len() + map() + split()

# initializing string
test_str = 'geeksforgeeks 33 is best'

# printing original string
print("The original string is : " + str(test_str))

# len() finds individual word Frequency
# sum() extracts final Frequency
res = sum(map(len, test_str.split()))
	
# printing result
print("The Characters Frequency avoiding spaces : " + str(res))


print('**************************')

# Python3 code to demonstrate working of
# Avoid Spaces in Characters Frequency


# initializing string
test_str = 'geeksforgeeks 33 is best'

# printing original string
print("The original string is : " + str(test_str))

test_str=test_str.replace(' ','')
res=len(test_str)
# printing result
print("The Characters Frequency avoiding spaces : " + str(res))
