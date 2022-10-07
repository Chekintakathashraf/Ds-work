class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # creation
    def createDLL(self,nodeValue):
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return "The DLL has been created"

    #insertion
    def insertDLL(self,value,location):
        newNode = Node(value)

        if self.head is None:
            print('the node cannot be inserted')
        else:
            if location ==0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location ==1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0

                while index < location -1:
                    tempNode = tempNode.next
                    index = index + 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode


    # traverse
    def traverseDLL(self):
        if self.head is None:
            print(" The singly linked list doesnot exit")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next    

    #reverse traverse
    def reversetraverseDLL(self):
        if self.head is None:
            print(" The singly linked list doesnot exit")
        else:
            node = self.tail
            while node is not None:
                print(node.value)
                node = node.prev

    # serching for node 
    def searchDLL(self,nodevalue):
        if self.head is None:
            return "The list does not exist"
        else: 
            tempnode = self.head
            while tempnode is not None:
                if tempnode.value == nodevalue:
                    return tempnode.value
                else:
                    tempnode = tempnode.next
            return "The value does not exist in this list"


    # delete node
    def deleteNode(self,location):
        if self.head is None:
            print("The doubly lingedlist doesnot exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location ==1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index = index + 1
                tempNode.next = tempNode.next.next
                tempNode.next.prev = tempNode


    # delete entire doubly linked list
    def deleteEntireDLL(self):
        if self.head is None:
            print("The DLL doesnot exist")
        else:
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None

            

dooublyLL = DoublyLinkedlist()

print("************  create   *****************")

dooublyLL.createDLL(1)

print([ node.value for node in dooublyLL])

print('**************  insertion  ***********************')

dooublyLL.insertDLL(0,0)
dooublyLL.insertDLL(5,1)
dooublyLL.insertDLL(2,1)
dooublyLL.insertDLL(3,2)
dooublyLL.insertDLL(4,0)

print([ node.value for node in dooublyLL])


print('***************  traverse   **********************')
dooublyLL.traverseDLL()

print('***************  reverse traverse   **********************')
dooublyLL.reversetraverseDLL()

print('****************   searching a node *********************')
print(dooublyLL.searchDLL(10))


print('****************   deleting a node by location *********************')

dooublyLL.deleteNode(0)
print([node.value for node in dooublyLL])

print('****************   deleting a node by location *********************')

dooublyLL.deleteEntireDLL()
print([node.value for node in dooublyLL])