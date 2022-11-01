def palindrome(string):
    string=string.lower().replace('','')
    return string==string[::-1]

print(palindrome('ambma'))