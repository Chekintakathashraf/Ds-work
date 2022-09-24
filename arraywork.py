from array import *

arr1 = array('i',[1,2,3,4,5,6])
print(arr1)
# arr1.insert(6,10)
# print(arr1)
# arr1.insert(0,0)
# print(arr1)
def traverseArray(array):
    for i in array:
        print(i)
# traverseArray(arr1)
def accessElement(array,index):
    if index >= len(array):
        print('There is not any element in this index')
    else:
        print(array[index])
# accessElement(arr1,19)
# accessElement(arr1,4)

def searchArray(array,value):
    for i in array:
        if i == value:
            return array.index(value)
    else:
            return 'The element doesnot exit in this array'
# print(searchArray(arr1,78))
# print(searchArray(arr1,6))

def removingArray(array,value):
    array.remove(value)
    print(array)

# removingArray(arr1,5)
# arr1.remove(3)
# print(arr1)

def removingArray(array,index):
    value=array[index]
    array.remove(value)
    print(array)

# removingArray(arr1,7)
