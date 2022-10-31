# Python – Uppercase Half String

# Python3 code to demonstrate working of
# Uppercase Half String
# Using upper() + loop + len()

# initializing string
test_str = 'geeksforgeeks'

# printing original string
print("The original string is : " + str(test_str))

# computing half index
hlf_idx = len(test_str) // 2

res = ''
for idx in range(len(test_str)):
	
    # uppercasing later half
    if idx >= hlf_idx:
        res += test_str[idx].upper()
    else:
	    res += test_str[idx]
		
# printing result
print("The resultant string : " + str(res))


print('*****************************')

# Python3 code to demonstrate working of
# Uppercase Half String
# Using list comprehension + join() + upper()

# initializing string
test_str = 'geeksforgeeks'

# printing original string
print("The original string is : " + str(test_str))

# computing half index
hlf_idx = len(test_str) // 2

# join() used to create result string
res = ''.join([test_str[idx].upper() if idx >= hlf_idx else test_str[idx]
		for idx in range(len(test_str)) ])
		
# printing result
print("The resultant string : " + str(res))


print('*****************')

# Python3 code to demonstrate working of
# Uppercase Half String
# Using upper() + slicing string

# initializing string
test_str = 'geeksforgeeks'

# printing original string
print("The original string is : " + str(test_str))

# computing half index
hlf_idx = len(test_str) // 2

# Making new string with half upper case
# Using slicing
# slicing takes one position less to ending position provided
res = test_str[:hlf_idx] + test_str[hlf_idx:].upper()
		
# printing result
print("The resultant string : " + str(res))
