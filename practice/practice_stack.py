import heapq
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


"""
연습문제 03
입력으로 들어온 문자열이 다음 집합의 원소인지 체크하는 코드를 스택을 이용해서 작성하시오.
"""
s_lst = list(input().split('$'))
stack = []
for char in s_lst[0]:
    stack.append(char)

for char in s_lst[1]:
    prev = stack.pop()
    if prev != char:
        stack.append(prev)

if stack:
    print("No")
else:
    print("Yes")
"""
연습문제 05
"""

def parenBalance(s:str) -> bool:
    stack = []
    for c in s:
        if c == ')' :
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
        stack.append(c)
    if stack:
        return False
    return True

print(parenBalance("(())"))

"""
보너스
"""

input_lst = list(map(int, input().split()))
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
