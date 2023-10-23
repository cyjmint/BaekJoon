n = int(input())
ans = [0]*(n+1)
ans[0] = 1; ans[1] = 3
for i in range(2,n):
    ans[i] = ans[i-1] + 2*ans[i-2]

print(ans[n-1]%10007)