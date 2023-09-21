from collections import deque

n = int(input())
people = deque(list(map(int,input().split())) for _ in range(n))

order = []
for _ in range(n):
    k = 1
    x,y = people[0]
    for i in range(1,n):
        a,b = people[i]
        if x<a and y<b:
            k += 1
    order.append(k)
    people.rotate(-1)
    
print(*order)