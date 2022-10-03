from platform import node


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class SLinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    #insertion
    def insertSLL(self,value,location):
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
            self.tail = newNode

        else:
            if location ==0:
                newNode.next = self.head
                self.head = newNode
            elif location ==1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0

                while index < location:
                    tempNode = tempNode.next
                    index = index + 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode




singlylinkedlist = SLinkedlist()

singlylinkedlist.insertSLL(1,0)
singlylinkedlist.insertSLL(2,0)
singlylinkedlist.insertSLL(3,0)
singlylinkedlist.insertSLL(4,1)

print([node.value for node in singlylinkedlist])
         