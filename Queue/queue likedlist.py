class Node:
    def __init__(self,value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class Queue:
    def __init__(self):
        self.LinkedList = Linkedlist()
    
    def __str__(self):
        values = [str(x) for x in self.LinkedList]
        return ' '.join(values)