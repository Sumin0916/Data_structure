# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RTtwtOFjz_XlMX5o3BfyuWNqijIKR7CH
"""

print("Hello python!")

def seq(n):
  if n == 1:
    return 1
  return seq(n-1)+3

seq(10)

def move(n, start, to, end):
  if n == 1:
    print(f"{n}번째 {start}를 {end}로 옮겼습니다.")
    return
  move(n-1, start, end, to)
  print(f"{n}번째 {start}를 {to}로 옮겼습니다.")
  move(n-1, end, to, start)

move(3, 'a', 'b', 'c')

mem = [-1 for _ in range(101)]
def pow(n):
  if n == 1:
    return 2
  if mem != -1:
    mem[n] = 2*pow(n-1)
    return mem[n]
  else:
    return mem[n]
  
print(pow(100))

maximum = -1
num = [2, 4, 1, 8, 9, 3]
def max(num, n):
  if n == 1:
    return num[0]
  return num[0] if num[0] > max(num[1:], n-1) else max(num[1:], n-1)

print(max(num, len(num)-1))

def is_included(string, sentence):
    words = list(sentence.split())
    if string in words:
      return "yes"
    else:
      return "no"

print(is_included("love", "I love you"))
print(is_included("me", "I love you"))
print(is_included("you", "I love you"))

def dosum():
  num = []
  for i in range(5):
    inp = input("type number:")
    num.append(inp)
  print(sum(num))
  return

  if __name__ == "__main__":
    dosum()

phone_book = {}

def insert(name, number):
  phone_book[name] = number
def delete(name):
  phone_book.pop(name, -1)
def search(name):
  print(phone_book[name])
def scan():
  for n,p in phone_book.items():
    print(n, p)

class employee():
  def __init__(self, name=None, salary=0):
    self.__name = name
    self.__salary = salary
    empcnt = 0
  #def