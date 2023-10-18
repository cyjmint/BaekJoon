t = int(input())
for _ in range(t):
    n = int(input())
    l = []
    l.append(1);l.append(2);l.append(4)
    for i in range(3,n):
        l.append(l[i-1]+l[i-2]+l[i-3])
    print(l[n-1])