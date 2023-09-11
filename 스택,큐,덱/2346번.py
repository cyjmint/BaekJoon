from collections import deque

n = int(input())
num = deque(map(int,input().split()))
num2 = deque(i for i in range(1,n+1))

temp = []
while len(num) > 0:
    a = num.popleft()
    temp.append(num2.popleft())
    if a > 0:
        num.rotate(1-a)
        num2.rotate(1-a)
    else:
        num.rotate(a*(-1))
        num2.rotate(a*(-1))
    
print(*temp)