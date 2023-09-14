n = int(input())
num = []
for _ in range(n):
    num.append(list(map(int,input().split())))
num = sorted(num)
for v in num:
    print(*v)