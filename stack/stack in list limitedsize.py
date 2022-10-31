
class Stack:
    def __init__(self,maxsize):
        self.maxsize = maxsize
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)


    #isEmpty

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    # is Full

    def isFull(self):
        if len(self.list) == self.maxsize:
            return True
        else:
            return False
    # push

    def push(self,value):
        if self.isFull():
            return "the stack is full"
        else:
            self.list.append(value)
            return "the element has been successfully inserted"

    # pop

    def pop(self):
        if self.isEmpty():
            return "the stack is empty"
        else:
            return self.list.pop()

    # peek 
    def peek(self):
        if self.isEmpty():
            return 'There is not any element in the stack'
        else:
            return self.list[len(self.list)-1]

    # delete
    def delete(self):
        self.list=None



customeStack = Stack(5)
print('************   isEmpty **************')

print(customeStack.isEmpty()) 

print('************   isFull **************')

print(customeStack.isFull()) 

print('************   push **************')
customeStack.push(1)
customeStack.push(2)
customeStack.push(3)
customeStack.push(4)
#customeStack.push(5)
#print(customeStack.push(6))
#print(customeStack)

print('************   pop **************')
customeStack.pop()
#print(customeStack)
print('************   peek **************')
print(customeStack.peek())

print('************   delete **************')
print(customeStack.delete())