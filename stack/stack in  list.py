
class Stack:
    def __init__(self):
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
    # push

    def push(self,value):
        self.list.append(value)
        return "the element has been successfully inserted"

    # pop

    def pop(self):
        if self.isEmpty():
            return 'There is not any element in the stack'
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

customeStack = Stack()
print('************   isEmpty **************')

print(customeStack.isEmpty()) 

print('************   push **************')
customeStack.push(1)
customeStack.push(2)
customeStack.push(3)
customeStack.push(4)

#print(customeStack)
print('************   pop **************')
customeStack.pop()
print(customeStack)
print('************   peek **************')
print(customeStack.peek())
print('************   delete **************')
print(customeStack.delete())