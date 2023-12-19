a,b = map(int,input().split())
ans = 1
for i in range(a,b+1):
    l = [j for j in range(1,i+1)]
    ans *= sum(l)

print(ans%14579)