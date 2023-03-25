import listlib as ll

a = ll.CircularDoublyLinkedList([0, 1, 2, 3])
b = ll.CircularDoublyLinkedList()
c = ll.CircularDoublyLinkedList()

a.append(4)
b.append(5)
b.append(6)
b.append(7)
print(a)
print(b)
print(a+b)
a = a+b
a.insert(0, -1)
print(a)
a.remove(-1)
print(a, a.size())
print(a.get(4))
print(a.index(3))
print(c.isEmpty())
a.clear()
print(a+b)
print(b+b)
b = b+b+b
print(b)
b.sort()
print(b)
a.sort()