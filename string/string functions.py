'''length - It provides the string’s length.

minimum - This function returns the smallest character in a string, as determined by ASCII.

maximum - The largest character found in the string, as determined by ASCII, is provided by the third option, maximum.

sorted - The string is sorted in either ascending or descending order using the ASCII character sequence. This function always returns a list of characters as its result.'''

s = 'GoodMorning'
print(len(s))
print(min(s))
print(max(s))
print(sorted(s))
print(sorted(s, reverse = True))

print('********************')

#capitalize

s = "its raining outside"
print(s.capitalize()) #O / P - > Its raining outside
print(s.title()) #O / P - > Its Raining Outside

print('********************')

#lowercase/upper/swap

s = "Its Raining Outside"
print(s.upper()) #O / P - > ITS RAINING OUTSIDE
print(s.lower()) #O / P - > its raining outside
print(s.swapcase()) #O / P - > iTS rAINING oUTSIDE

print('********************')
#count

s = "Its Raining Outside"
print(s.count("i")) #3
print(s.count("ing")) # 1

print('********************')

#find index

s = "Its Raining Outside"
print(s.find("ing")) #8
print(s.index("ing")) # 8
print(s.find("down")) # - 1
# print(s.index("down")) #error