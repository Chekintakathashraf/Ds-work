#addition

s = "Good" + "-" + "Morning"
print(s)
print('********************')

#multiplication

s = "Good"
print(s * 3)
print('********************')

#relational operation

print("Hello" == "World")
print("Hello" != "World")
print('********************')
print("Mumbai" > "Pune")
print("Goa" < "Indore")
print('********************')

#logical operation

'''When you use the AND, OR, and NOT logical operators on strings, Python returns false for empty strings and true for non-empty strings.'''

print("Hello"
  and "World") #True and True - > True(O / P - > World)
print(""
  and "World") #False and True - > False(O / P - > "")
print(""
  or "World") #False OR True - > True(O / P - > "World")
print(not "Hello") #opposite of True - > False
print(not "") #True

print('********************')
#loop

s = 'GoodMorning'
for i in s:
  print(i)

print('********************')

#membership operator

s = 'GoodMorning'
if 'M' in s:
  print('true')

print('********************')


