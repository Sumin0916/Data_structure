"""
연습문제 02
"""

class ListStack:
    def __init__(self):
        self.__stack = []
    def push(self, x):
        self.__stack.append(x)
    def pop(self):
        return self.__stack.pop(0)
    def top(self):
        if self.isEmpty():
            print("No element in stack")
            return None
        else:
            return self.__stack[0]
    def isEmpty(self) -> bool:
        return not bool(self.__stack)
    def popAll(self):
        self.__stack.clear()
    def printStack(self):
        print("Stack:")
        for i in range(len(self.__stack)):
            print(f"stack[{i}]: {self.__stack[i]}")

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

"""
연습문제 03
입력으로 들어온 문자열이 다음 집합의 원소인지 체크하는 코드를 스택을 이용해서 작성하시오.
"""
s_lst = list(input().split('$'))
LS = LinkedStack()
for char in s_lst[0]:
    LS.push(char)

for char in s_lst[1]:
    prev = LS.top()
    if prev != char:
        LS.push(char)
    else:
        LS.pop()

if LS.is_empty():
    print("Yes")
else:
    print("No")
print()

"""
연습문제 05
"""

def parenBalance(s:str) -> bool:
    LS = LinkedStack()
    for c in s:
        if c == '(':
            LS.push(c)
        elif c == ')' :
            if LS.top() == '(' and not LS.is_empty():
                LS.pop()
            else:
                LS.push(c)
    if LS.is_empty():
        return True
    return False

print(parenBalance("((800/ (3+5)*2)"))
print(parenBalance("(82+2)/4)"))
print(parenBalance("(91*(40-35)+2)"))
print()

"""
연습문제 06
"""
def parenBalance2(s:str) -> bool:
    LS = LinkedStack()
    d = {')':0, ']':1, '}':2}
    opened = ['(', '[', '{']
    closed = [')', ']', '}']
    for c in s:
        if c in opened:
            LS.push(c)
        elif c in closed:
            if LS.top() == opened[d[c]] and not LS.is_empty():
                LS.pop()
    if LS.is_empty():
        return True
    return False

print(parenBalance2("[91*(40-35)+2]"))
print(parenBalance("[82+2)/4}"))
print()
"""
보너스
"""

#input_lst = list(map(int, input().split()))
input_lst = [1, 5, 4, 3, 2]
stack = [input_lst[0]]
for num in input_lst[1:]:
        prev = stack.pop()
        if prev <= num:
            stack.append(prev)
            stack.append(num)
        else:
            stack.append(num)
            stack.append(prev)
print(stack)
print(stack.pop())
