from collections import deque

n = int(input())
queue = deque()
for _ in range(n):
    order = list(input().split())
    a = order[0]
    if len(order) > 1:
        b = int(order[1])
        
    if a == 'push':
        queue.append(b)
    
    elif a == 'pop':
        if len(queue) != 0:
            print(queue.popleft())
        else:
            print(-1)
    
    elif a == 'size':
        print(len(queue))
    
    elif a == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    
    elif a == 'front':
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
    
    elif a == 'back':
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)