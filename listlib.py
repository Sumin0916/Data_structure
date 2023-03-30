from heapq import heappop, heappush

class BidirectNode:
    def __init__(self, item: dict, prevNode: 'BidirectNode', nextNode:'BidirectNode'):
        self.item = item
        self.prev = prevNode
        self.next = nextNode

class CircularDoublyLinkedList:
    def __init__(self, *arg):
        self.__head = BidirectNode(None, None, None)
        self.__head.prev = self.__head
        self.__head.next = self.__head
        self.__numItems = 0
        if len(arg) != 0:
            for item in arg[0]:
                self.append(item)

    def __iter__(self):
        return CircularLinkedListIterator(self)

    def __add__(self, canIterate) -> 'CircularDoublyLinkedList':
        tempList = self.copy()
        return tempList.extend(canIterate)

    def __str__(self):
        slst = []
        for item in self:
            slst.append(str(item))
        return '[' + ', '.join(slst) + ']'

    def getNode(self, i:int) -> BidirectNode: #성공시 해당 인덱스 노드 가져오기, 실패시 더미노드 가져오기
        if (i > self.__numItems):
            print(f"index : {i} is out of boundery")
            return self.__head
        curr = self.__head
        for _ in range(i+1):
            curr = curr.next
        return curr

    def insert(self, i:int, newItem) -> None: #인덱스 번호에 노드 삽입
        if (i >= 0 and i <= self.__numItems):
            prev = self.getNode(i-1)
            newNode = BidirectNode(newItem, prev, prev.next)
            prev.next = newNode
            newNode.next.prev = newNode
            self.__numItems += 1
        else:
            print(f"index : {i} is out of boundery")
        return None

    def append(self, newItem) -> None: #무조건 추가 가능
        prev = self.__head.prev
        newNode = BidirectNode(newItem, prev, self.__head)
        self.__head.prev = newNode
        prev.next = newNode
        self.__numItems += 1

    def pop(self, *arg): #성공시 해당 인덱스 노드의 값 반환, 실패시 None 반환
        if self.isEmpty():
            print("There is no elements")
            return None
        if len(arg) != 0:
            index = arg[0]
        if (len(arg) == 0 or index == -1):
            curr = self.__head.prev
        elif (-1 < index and index < self.__numItems):
            curr = self.getNode(index)
        else:
            print(f"index : {index} is out of boundery")
            return None
        retItem = curr.item
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
        self.__numItems -= 1
        return retItem
            
    def remove(self, x): #X가 있는 노드 제거 성공시 X 반환, 실패시 None 반환
        curr = self.__findNode(x)
        if curr.item != None:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            self.__numItems -= 1
            return x
        else:
            return None

    def get(self, *arg): #해당 인덱스 노드 값 반환, 실패시 None 반환
        if len(arg) != 0:
            index = arg[0]
            curr = self.getNode(index)
        elif len(arg) == 0 or index == -1:
            curr = self.__head.prev
        return curr.item

    def index(self, x): #값이 있을 시 해당 인덱스 반환, 실패시 None 반환
        for index, item in enumerate(self):
            if item == x:
                return index
        return None

    def isEmpty(self) -> bool: #비어있으면 참, 아니면 거짓을 반환한다.
        return self.__numItems == 0

    def size(self) -> int: #리스트의 길이를 반환한다.
        return self.__numItems

    def clear(self): #연결 초기화
        self.__head = BidirectNode(None, None, None)
        self.__head.prev = self.__head
        self.__head.next = self.__head
        self.__numItems = 0

    def count(self, x) -> int: #X값의 개수를 반환한다.
        cnt = 0
        for item in self:
            if item == x:
                cnt += 1
        return cnt

    def extend(self, canIterate) -> 'CircularDoublyLinkedList': #순환가능 객체면 확장시켜준다. 객체가 CircularDoublyLinkedList면 최적화 확장을 한다.
        if type(canIterate) is CircularDoublyLinkedList:
            tempList = canIterate.copy()
            if tempList.size == 0:
                return self
            lastNode = self.__head.prev
            lastNode.next = tempList.__head.next
            tempList.__head.prev.next = self.__head
            self.__numItems += tempList.__numItems
        else:
            for item in canIterate:
                self.append(item)
        return self

    def copy(self) -> 'CircularDoublyLinkedList':
        newObject = CircularDoublyLinkedList()
        for item in self:
            newObject.append(item)
        return newObject

    def reverse(self) -> 'CircularDoublyLinkedList':
        curr = self.__head
        curr.prev, curr.next = curr.next, curr.prev
        for _ in range(self.__numItems):
            curr = curr.next
            curr.prev, curr.next = curr.next, curr.prev
        return self

    def sort(self) -> None:
        selfList = []
        lenList = self.__numItems
        for item in self:
            heappush(selfList, item)
        self.clear()
        for _ in range(lenList):
            self.append(heappop(selfList))

    def __findNode(self, x) -> BidirectNode: #해당 값이 있는 가장 작은 인덱스 노드를 반환, 없으면 더미노드 반환
        curr = self.__head.next
        while curr != self.__head:
            if (curr.item == x):
                return curr
            curr = curr.next
        return self.__head

    def printList(self) -> None:
        for item in self:
            print(item, end=' ')
        print()
    
class CircularLinkedListIterator: #'CircularDoublyLinkedList' 순회자 객체
    def __init__(self, clObject):
        self.__head = clObject.getNode(-1)
        self.iterPosition = self.__head.next

    def __next__(self):
        if self.iterPosition == self.__head:
            raise StopIteration
        else:
            item = self.iterPosition.item
            self.iterPosition = self.iterPosition.next
            return item

# class CircularDoublyLinkedListFilter:

