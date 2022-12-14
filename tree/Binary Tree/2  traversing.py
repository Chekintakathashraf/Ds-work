class TreeNode:
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None

newBT =  TreeNode("Drinks")


leftChild=TreeNode("Hot")
rightChild=TreeNode("Cold")

newBT.leftChild=leftChild
newBT.rightChild=rightChild

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

preOrderTraversal(newBT)

print('***************')

def inOrderTraversal(rootNode):
    if not rootNode:
        return
   
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

inOrderTraversal(newBT)

print('***************')

def postOrderTraversal(rootNode):
    if not rootNode:
        return
   
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

postOrderTraversal(newBT)