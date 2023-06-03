class BinarySearchTree:
    def __init__(self, *arg):
        self.__root = None

    def search(self, x) -> "TreeNode":
        return self.__loopSearch(self.__root, x)

    def __searchItem(self, tNode:"TreeNode", x):
        if tNode == None:
            return None
        elif x == tNode.item:
            return tNode
        elif x < tNode.item:
            return self.__searchItem(tNode.left, x)
        else:
            return self.__searchItem(tNode.right, x)
    
    def __loopSearch(self, tNode:"TreeNode", x):
        nowNode = tNode
        while nowNode != None:
            if nowNode.item == x:
                return nowNode
            elif nowNode.item < x:
                nowNode = nowNode.right
            else:
                nowNode = nowNode.left
        return None
            
    def insert(self, newItem):
        self.__root = self.__insertItem(self.__root, newItem)

    def __insertItem(self, tNode:"TreeNode", newItem):
        if tNode == None:
            return TreeNode(newItem, None, None)
        elif newItem < tNode.item:
            tNode.left = self.__insertItem(tNode.left, newItem)
        else:
            tNode.right = self.__insertItem(tNode.right, newItem)
        return tNode

    def delete(self, x):
        self.__root = self.__deleteItem(self.__root, x)

    def __deleteItem(self, tNode:"TreeNode", x):
        if tNode == None:
            return None
        elif x == tNode.item:
            tNode = self.__deleteNode(tNode)
        elif x < tNode.item:
            tNode.left = self.__deleteItem(tNode.left, x)
        else:
            tNode.right = self.__deleteItem(tNode.right, x)
        return tNode

    def __deleteNode(self, tNode:"TreeNode"):
        if tNode.left == None and tNode.right == None:
            return None
        elif tNode.left == None:
            return tNode.right
        elif tNode.right == None:
            return tNode.left
        else: #둘 다 있을 때
            (rtnItem, rtnNode) = self.__deleteMinItem(tNode.right)
            tNode.item = rtnItem
            tNode.right = rtnNode
            return tNode

    def __deleteMinItem(self, tNode:"TreeNode"):
        if tNode.left == None:
            return (tNode.item, tNode.right)
        else:
            (rtnItem, rtnNode) = self.__deleteMinItem(tNode.left)
            tNode.left = rtnNode
            return (rtnItem, tNode)

    def isEmpty(self):
        return self.__root == None

    def clear(self):
        self.__root = None
    
    def getRoot(self):
        return self.__root

    def inorder(self, rNode):
        if rNode == None:
            return
        self.inorder(rNode.left)
        print(rNode.item, end=' ')
        self.inorder(rNode.right)

class TreeNode:
    def __init__(self, newItem, left, right):
        self.item = newItem
        self.left = left
        self.right = right

bst1 = BinarySearchTree()
bst1.insert(10)
bst1.insert(20)
bst1.insert(5)
bst1.insert(80)
bst1.insert(90)
bst1.insert(7550)
bst1.insert(30)
bst1.insert(77)
bst1.insert(15)
bst1.insert(40)
bst1.delete(7550)
bst1.delete(10)
bst1.inorder(bst1.getRoot())
print(bst1.search(40).item)