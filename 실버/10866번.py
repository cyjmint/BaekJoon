from collections import deque

n = int(input())
d = deque()
for _ in range(n):
    order = list(input().split())
    a = order[0]
    if len(order) > 1:
        b = int(order[1])
        
    if a == 'push_front':
        d.appendleft(b)
    
    elif a == 'push_back':
        d.append(b)
        
    elif a == 'pop_front':
        if len(d) != 0:
            print(d.popleft())
        else:
            print(-1)
            
    elif a == 'pop_back':
        if len(d) != 0:
            print(d.pop())
        else:
            print(-1)
    
    elif a == 'size':
        print(len(d))
    
    elif a == 'empty':
        if len(d) == 0:
            print(1)
        else:
            print(0)
    
    elif a == 'front':
        if len(d) != 0:
            print(d[0])
        else:
            print(-1)
    
    elif a == 'back':
        if len(d) != 0:
            print(d[-1])
        else:
            print(-1)