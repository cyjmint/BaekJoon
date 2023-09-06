from collections import deque

n = int(input())
queue = deque()
for _ in range(n):
    order = input().split()
    if order[0] == 'push':
        queue.appendleft(order[1])
    
    elif order == ['pop']:
        if len(queue) != 0:
            print(queue.pop())
        else:
            print(-1)
        
    elif order == ['size']:
        print(len(queue))
    
    elif order == ['empty']:
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif order == ['front']:
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)

    else:
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)