class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack:
    def __init__(self):
        self.head = None
        self.__numItems = 0
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.__numItems += 1

    def pop(self):
        if self.is_empty():
            return -1
        data = self.head.data
        self.head = self.head.next
        self.__numItems -= 1
        return data
    
    def is_empty(self):
        if self.head:
            return False
        return True
    
    def top(self):
        if self.is_empty():
            return -1
        return self.head.data
    
    def size(self):
        return self.__numItems

class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.__numItems = 0

    def push(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.__numItems += 1

    def dequeue(self):
        if self.is_empty():
            return -1
        if self.size() == 1:
            self.tail = None
        data = self.head.data
        self.head = self.head.next
        self.__numItems -= 1
        return data
    
    def is_empty(self):
        if self.head:
            return False
        return True
    
    def top(self):
        if self.is_empty():
            return -1
        return self.head.data
    
    def size(self):
        return self.__numItems

"""
연습문제 02
입력으로 들어온 문자열이 다음 집합의 원소인지{w|w} 체크하는 코드를 큐를 이용해서 작성하시오.
"""
print("-- 2 --")
s_lst = list(input().split('$'))
LS = LinkedQueue()
for char in s_lst[0]:
    LS.push(char)

for char in s_lst[1]:
    prev = LS.top()
    if prev != char:
        LS.push(char)
    else:
        LS.dequeue()

if LS.is_empty():
    print("Yes")
else:
    print("No")
print()

"""
연습문제 04
2개의 큐를 사용하여 스택의 Push와 Pop 알고리즘을 작성하시오
"""

class TwoQueueStack():
    def __init__(self):
        self.__q = LinkedQueue()
        self.__tq = LinkedQueue()
    def __MoveQueue(self, q, tq):
        while not q.is_empty():
            tq.push(q.dequeue())
    def push(self, x):
        self.__MoveQueue(self.__q, self.__tq)
        self.__q.push(x)
        self.__MoveQueue(self.__tq, self.__q)

    def pop(self):
        return self.__q.dequeue()
print("-- 4 --")
a = TwoQueueStack()
a.push(1)
a.push(2)
a.push(3)
print(a.pop())
print(a.pop())
print(a.pop())
print()
"""
연습문제 04 변형 push를 O(1)로 만드시요.
"""

class OptimizePushStack():
    def __init__(self):
        self.__q = LinkedQueue()
        self.__tq = LinkedQueue()
    def __MoveQueueRemainOne(self, q, tq):
        while not q.size() == 1:
            tq.push(q.dequeue())
    def push(self, x):
        self.__q.push(x)

    def pop(self):
        self.__MoveQueueRemainOne(self.__q, self.__tq)
        tmp = self.__q.dequeue()
        self.__MoveQueueRemainOne(self.__tq, self.__q)
        return tmp

"""
연습문제 05
2개의 스택을 사용하여 enqueue()와 dequeue()를 구현하시오.
"""

class TwoStackQueue():
    def __init__(self):
        self.__s = LinkedStack()
        self.__ts = LinkedStack()
    def __MoveStack(self, s, ts):
        while not s.is_empty():
            ts.push(s.pop())
    def push(self, x):
        self.__MoveStack(self.__s, self.__ts)
        self.__s.push(x)
        self.__MoveStack(self.__ts, self.__s)

    def pop(self):
        return self.__s.pop()

b = TwoStackQueue()
print("-- 5 --")
b.push(1)
b.push(2)
b.push(3)
print(b.pop())
print(b.pop())
print(b.pop())
print()

"""
보너스 문제
A항공사는 고객 등급을 일, 골, 플 회원으로 나누어 관리. 비행기 탑승 시 등급이 높은 순서대로 탑승. 동일 등급 내에서는
도착한 순서대로 탑승. 고객이 도착했을 때 위와 같은 순서로 탑승을 하려면 어떤 자료구조를 어떻게 사용해야 하는가?
"""

"""
Solution 1)
0. 등급마다 큐를 만듬.
1. 고객이 온 순서대로 등급을 확인하며 해당 등급 큐에 추가.
2. 높은 등급의 큐부터 순서대로 고객들을 호출함.
3. 큐가 비면 그 아래 등급 큐에서 고객 호출 (제일 낮은 등급 큐까지)

삽입, 삭제 -> O(1)

Solution 2)
0. 고객 등급에 따라 값 설정 ex) 일반 : 3, 골드 : 2, 플레티넘 : 1
1. 가중치 값 설정 문자열 결합 -> 가중치 = int(str(등급) + str(순서)) ex) 3 + 21 = 321
2. 고객이 도착한 순서대로 우선순위 큐에 가중치를 토대로 삽입
3. 우선순위 큐 순서대로 고객들을 재배치
4. 고객들을 비행기에 탑승시킴

우선순위 큐 -> 힙 자료구조 이용
삽입, 삭제 - > O(1ogN)
"""
