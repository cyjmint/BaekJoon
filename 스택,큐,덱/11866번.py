from collections import deque

n,k = map(int,input().split())
queue = deque(i for i in range(1,n+1))
ans = []

while len(queue) > 0:
    num = 1
    while num < k:
        queue.append(queue[0])
        queue.popleft()
        num += 1
    ans.append(queue[0])
    queue.popleft()
    
a = f'{ans[0]}'
for i in range(1,n):
    a += ', '+f'{ans[i]}'
    
print(f'<{a}>')