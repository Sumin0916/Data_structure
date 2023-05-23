system = list(input("Input string: ").split())
operator = ['+', '-', '*', '/']
stack = []
for string in system:
    if string not in operator:
        stack.append(string)
    else:
        b=stack.pop(); a=stack.pop()
        stack.append(str(eval(a+string+b)))
print(stack[0])
