from collections import deque

n = int(input())
stack = deque()
for _ in range(n):
    order = list(input().split())
    a = order[0]
    if len(order) == 2:
        b = int(order[1])
        
    if a == 'push':
        stack.append(b)
    
    elif a == 'pop':
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)
    
    elif a == 'size':
        print(len(stack))
    
    elif a == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    
    elif a == 'top':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)