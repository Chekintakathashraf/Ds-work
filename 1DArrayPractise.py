from array import *

Myarray = array('i', [1,2,3,3,4,5])
print(Myarray)

# 1. Traverse array

def traveseArray(array):
    for i in array:
        print(i)
# traveseArray(Myarray)

# 2. Access an individual array usng index

def accessArray(array,index):
    value=array[index]
    print(value)
# accessArray(Myarray,3)

# 3. Insert any value to the array using append() method

def appendArray(array,value):
    array.append(value)
    print(array)
# appendArray(Myarray,2)

# 4. Insert any value to the array using insert() method

def insertArray(array,index,value):
    array.insert(index,value)
    print(array)
# insertArray(Myarray,3,10)

#5 Extend python array using extend() method

def extendArray(array,arrayex):
    array.extend(arrayex)
    print(array)

# myarray2=array('i',[20,30,40])
# extendArray(Myarray,myarray2)

#6 Add item from list into array using fromlist() method

def fromlistArray(array,list):
    array.fromlist(list)
    print(array)
# mylist = [20,30,40]
# fromlistArray(Myarray,mylist)

#7 remove any array element using remove() method

def removeArray(array,value):
    array.remove(value)
    print(array)
# removeArray(Myarray,3)

#8 remove last array element using pop() method

def removePopArray(array):
    array.pop()
    print(array)
# removePopArray(Myarray)

#9 fetch any elment through its index using index() method

def printindexArray(array,value):
    ans=array.index(value)
    print(ans)
# printindexArray(Myarray,5)

#10 Reverse an array using reverse() method

def reverseArray(array):
    array.reverse()
    print(array)

# reverseArray(Myarray)

#11 Get array buffer information through buffer_info() method

def bufferInfo(array):
    ans=array.buffer_info()
    print(ans)
# it give first the  ( all buffer starts from this point , numer of elements)

# bufferInfo(Myarray)

#12 Check for number of occurance of elements using count() method

def occuranceArray(array,value):
    ans=array.count(value)
    print(ans)

# occuranceArray(Myarray,3)

#13 Convert array to list using tolist() method

def toListArray(array):
    ans=array.tolist()
    print(ans)

# toListArray(Myarray)

