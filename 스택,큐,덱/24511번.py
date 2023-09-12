from collections import deque
#import sys
#input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
m = int(input())
c = deque(map(int,input().split()))

b2 = deque()
for i in range(n):
    if a[i] == 0:
        b2.append(b[i])
    
x = []
if len(b2) >= m:
    for _ in range(m):
        x.append(b2.pop())
else:
    for _ in range(len(b2)):
        x.append(b2.pop())

if len(x) != m:
    for _ in range(m-len(x)):
        x.append(c.popleft())
        
print(*x)