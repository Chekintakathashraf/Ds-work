from Queue.queuelikedlist import Queue as queue

class TreeNode:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None

newBT =  TreeNode("Drinks")

leftChild=TreeNode("Hot")
tea= TreeNode("Tea")
coffee= TreeNode("Cofee")

leftChild.leftchild=tea
leftChild.rightchild=coffee

rightChild=TreeNode("Cold")


newBT.leftChild=leftChild
newBT.rightChild=rightChild

def searchBT(rootNode,nodeValue):
    if not rootNode:
        return "The BT doesnot exist"

    else:
        customQueue=queue.Queue()
        customQueue.enque(rootNode)
        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            if root.value.data == nodeValue:
                return "Success"
            if (root.value.rightChild is not None):
                customQueue.enque(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
        return "Not Found "

print(searchBT(newBT,"Cola"))