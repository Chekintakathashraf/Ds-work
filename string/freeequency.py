# Frequency of numbers in String

# Python3 code to demonstrate working of
# Frequency of numbers in String
# Using re.findall() + len()
import re

# initializing string
test_str = "geeks4feeks is No. 1 4 geeks"

# printing original string
print("The original string is : " + test_str)

# Frequency of numbers in String
# Using re.findall() + len()
res = len(re.findall(r'\d+', test_str))

# printing result
print("Count of numerics in string : " + str(res))

print('******************')

# Python3 code to demonstrate working of
# Frequency of numbers in String
# Using re.findall() + sum()
import re

# initializing string
test_str = "geeks4feeks is No. 1 4 geeks"

# printing original string
print("The original string is : " + test_str)

# Frequency of numbers in String
# Using re.findall() + sum()
res = sum(1 for _ in re.finditer(r'\d+', test_str))

# printing result
print("Count of numerics in string : " + str(res))


print('*******************')

# Python3 code to demonstrate working of
# Frequency of numbers in String

# initializing string
test_str = "geeks4feeks is No. 1 4 geeks"

# printing original string
print("The original string is : " + test_str)

# Frequency of numbers in String
res=0
for i in test_str:
	if(i.isdigit()):
		res+=1
# printing result
print("Count of numerics in string : " + str(res))
