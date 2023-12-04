t = int(input())
for _ in range(t):
    n = int(input())
    ans = []
    l = list(reversed(list(bin(n))))
    for i in range(len(l)-2):
        if l[i] == '1':
            ans.append(i)
    print(*ans)