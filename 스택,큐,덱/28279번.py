from collections import deque
n = int(input())
d = deque()

for _ in range(n):
    order = list(map(int,input().split()))
    
    if order[0] == 1:
        d.appendleft(order[1])
    elif order[0] == 2:
        d.append(order[1])
        
    elif order[0] == 3:
        if len(d) != 0:
            print(d.popleft())
        else:
            print(-1)
    elif order[0] == 4:
        if len(d) != 0:
            print(d.pop())
        else:
            print(-1)
    
    elif order[0] == 5:
        print(len(d))
    
    elif order[0] == 6:
        if len(d) == 0:
            print(1)
        else:
            print(0)
    
    elif order[0] == 7:
        if len(d) != 0:
            print(d[0])
        else:
            print(-1)
    else:
        if len(d) != 0:
            print(d[-1])
        else:
            print(-1)