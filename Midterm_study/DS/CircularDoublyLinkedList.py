from ListNode import BidirectNode

class CirculatDoublyLinkedList:
    def __init__(self):
        self.__head = BidirectNode(None, None, None)
        self.__numItems = 0
        self.__head.prev = self.__head
        self.__head.next = self.__head

    def insert(self, i:int, newItem) -> None:
        if 0 <= i <= self.__numItems:
            prev = self.getNode(i-1)
            newNode = BidirectNode(newItem, prev, prev.next)
            newNode.next.prev = newNode
            prev.next = newNode
            self.__numItems += 1
        else:
            print(f"Index Error : {i} is out of boundary")
    
    def append(self, newItem) -> None:
        tail = self.__head.prev
        newNode = BidirectNode(newItem, tail, self.__head)
        tail.next = newNode
        self.__head.prev = newNode
        self.__numItems += 1
    
    def pop(self, ind = -1):
        if self.isEmpty():
            return None
        if ind == -1 or ind == self.__numItems-1:
            delNode = self.__head.prev
        elif -1 < ind < self.__numItems-1:
            delNode = self.getNode(ind)
        else:
            print(f"Index Error : {ind} is out of boundary")
            return None
        self.__head.prev = delNode.prev
        delNode.prev.next = self.__head
        self.__numItems -= 1
        return delNode.item

    def remove(self, item):
        delNode = self.__findNode(item)
        if delNode == None:
            print(f"Index Error : {ind} is out of boundary")
            return
        delNode.prev.next = delNode.next
        delNode.next.prev = delNode.prev
        self.__numItems -= 1
        return item
    
    def get(self, ind = -1):
        if self.isEmpty():
            return None
        if ind == -1 or ind == self.__numItems-1:
            getNode = self.__head.prev
        elif -1 < ind < self.__numItems-1:
            getNode = self.getNode(ind)
        else:
            print(f"Index Error : {ind} is out of boundary")
            return None
        return getNode.item

    def index(self, x):
        count = 0
        for item in self:
            if item == x:
                return count
            count += 1
        return None

    def size(self) -> int:
        return self.__numItems
    
    def printList(self) -> None:
        print('[',end="")
        for item in self:
            print(f"{item} ", end="")
        print(']')
        
    def getNode(self, ind:int) -> BidirectNode:
        nNode = self.__head
        for i in range(ind+1):
            nNode = nNode.next
        return nNode
    
    def isEmpty(self) -> bool:
        if self.__numItems == 0:
            return True
        return False
    
    def clear(self):
        self.head = BidirectNode(None, None, None)
        self.head.next = self.head
        self.head.prev = self.head
        self.__numItems = 0

    def count(self, x) -> int:
        counter = 0
        for item in self:
            if item == x:
                counter += 1
        return counter

    def extend(self, iterable):
        for item in iterable:
            self.append(item)

    def copy(self) -> 'CirculatDoublyLinkedList':
        temp = CirculatDoublyLinkedList()
        for item in self:
            temp.append(item)
        return temp

    def reverse(self):
        prev = self.__head; curr = prev.next; nex = curr.next
        for _ in range(self.__numItems):
            curr.next = prev; curr.prev = nex
            prev = curr; curr = nex; nex = nex.next

    def __findNode(self, item) -> BidirectNode:
        curr = self.__head.next
        while curr != self.__head:
            if curr.item == item:
                return curr
            curr = curr.next
        return None

    def __iter__(self):
        return CirculatDoublyLinkedListIterator(self)

class CirculatDoublyLinkedListIterator:
    def __init__(self, alist:'CirculatDoublyLinkedList'):
        self.head = alist.getNode(-1)
        self.iterPosition = self.head.next
    
    def __next__(self):
        if self.iterPosition == self.head:
            return StopIteration
        item = self.iterPosition.item
        self.iterPosition = self.iterPosition.next
        return item
