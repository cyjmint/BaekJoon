n = int(input())
wine = [int(input()) for _ in range(n)]
dp = [0]*10000
dp[0] = wine[0]

if n > 1:
    dp[1] = wine[1] + dp[0]
    for i in range(2,n):
        dp[i] = max(wine[i] + dp[i-2], wine[i] + wine[i-1] + dp[i-3], dp[i-1])

print(dp[n-1])