class BinarySearchTree:
    def __init__(self, *arg):
        self.__root = None
    def search(self, x) -> "TreeNode":
        return self.__searchItem(self.__root, x)
    def __searchItem(self, tNode:"TreeNode", x):
        if tNode == None:
            return None
        elif x == tNode.item:
            return tNode
        elif x < tNode.item:
            return self.__searchItem(tNode.left, x)
        else:
            return self.__searchItem(tNode.right, x)

    def insert(self, newItem):
        self.__root = self.__insertItem(self.root, newItem)
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

    def isEmpty(self):
    def clear(self):

class TreeNode:
    def __init__(self, newItem, left, right):
        self.item = newItem
        self.left = left
        self.right = right

