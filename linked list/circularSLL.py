from platform import node


class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

class CircularSinglyLinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    # creation
    def createCSLL(self,nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "The CSLL has been created"

    #insertion
    def insertCSLL(self,value,location):
        

        if self.head is None:
            return "The head reference is None"

        else:
            newNode = Node(value)
            if location ==0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location ==1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0

                while index < location - 1:
                    tempNode = tempNode.next
                    index = index + 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
        return " The node has been successfully inserted"
    # traverse
    def traverseSLL(self):
        if self.head is None:
            print(" The singly linked list doesnot exit")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next
                if node == self.tail.next:
                    break

    # serching for node 
    def searchSLL(self,nodevalue):
        if self.head is None:
            return "The list does not exist"
        else: 
            node = self.head
            while node is not None:
                if node.value == nodevalue:
                    return node.value
                else:
                    node = node.next
                if node == self.tail.next:
                    return "The value does not exist in this list"

    # delete node
    def deleteNode(self,location):
        if self.head is None:
            print("The circularsinglylingedlist doesnot exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        else:
                            node= node.next
                    node.next = self.head
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index = index + 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next


    # delete entire circular singly linked list
    def deleteEntireSLL(self):
        if self.head is None:
            print("The SLL doesnot exist")
        else:
            self.head = None
            self.head = None
            self.tail.next = None

circularSLL = CircularSinglyLinkedlist()

print('**************  creating CSLL **************')

circularSLL.createCSLL(1)

print([ node.value for node in circularSLL])

print('**************  inserting CSLL **************')

circularSLL.insertCSLL(0,0)
circularSLL.insertCSLL(2,1)
circularSLL.insertCSLL(3,1)
circularSLL.insertCSLL(4,0)
circularSLL.insertCSLL(5,2)

print([ node.value for node in circularSLL])

print('***************  traverse   **********************')
circularSLL.traverseSLL()

print('****************   searching a node *********************')
print(circularSLL.searchSLL(5))

print('****************   deleting a node by location *********************')

circularSLL.deleteNode(1)
print([ node.value for node in circularSLL])

print('****************   deleting entire list *********************')

circularSLL.deleteEntireSLL()
print([node.value for node in circularSLL])