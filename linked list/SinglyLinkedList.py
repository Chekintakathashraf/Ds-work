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

    # traverse
    def traverseSLL(self):
        if self.head is None:
            print(" The singly linked list doesnot exit")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next
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
            return "The value does not exist in this list"

    # delete node
    def deleteNode(self,location):
        if self.head is None:
            print("The singlylingedlist doesnot exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location ==1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        else:
                            node= node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index = index + 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next

    # delete entire singlylinked list
    def deleteEntireSLL(self):
        if self.head is None:
            print("The SLL doesnot exist")
        else:
            self.head = None
            self.head = None




singlylinkedlist = SLinkedlist()

print('**************  insertion  ***********************')

singlylinkedlist.insertSLL(1,1)
singlylinkedlist.insertSLL(2,1)
singlylinkedlist.insertSLL(3,1)
singlylinkedlist.insertSLL(4,1)


print([node.value for node in singlylinkedlist])

print('***************  traverse   **********************')
singlylinkedlist.traverseSLL()


print('****************   searching a node *********************')
print(singlylinkedlist.searchSLL(5))


print('****************   deleting a node by location *********************')

singlylinkedlist.deleteNode(2)
print([node.value for node in singlylinkedlist])

print('****************   deleting entire list *********************')

singlylinkedlist.deleteEntireSLL()
print([node.value for node in singlylinkedlist])

