n = int(input())
num = list(map(int,input().split()))

ans = 0
for v in num:
    if n == v:
        ans += 1

print(ans)