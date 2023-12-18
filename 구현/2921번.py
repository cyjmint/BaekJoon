n = int(input())
ans = 0
for i in range(1,n+1):
    for j in range(i,i*2+1):
        ans += j
print(ans)