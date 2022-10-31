#  Least Frequent Character in String

'''Method 1 : Naive method + min() '''

# Python 3 code to demonstrate
# Least Frequent Character in String
# naive method

# initializing string
test_str = "GeeksforGeeks"

# printing original string
print ("The original string is : " + test_str)

# using naive method to get
# Least Frequent Character in String
all_freq = {}
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
        res = min(all_freq, key = all_freq.get)

# printing result
print ("The minimum of all characters in GeeksforGeeks is : " + str(res))


print('*****************************')

'''Method 2 : Using collections.Counter() + min() '''

# Python 3 code to demonstrate
# Least Frequent Character in String
# collections.Counter() + min()
from collections import Counter

# initializing string
test_str = "GeeksforGeeks"

# printing original string
print ("The original string is : " + test_str)

# using collections.Counter() + min() to get
# Least Frequent Character in String
res = Counter(test_str)
res = min(res, key = res.get)

# printing result
print ("The minimum of all characters in GeeksforGeeks is : " + str(res))
