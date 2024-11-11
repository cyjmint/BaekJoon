t = int(input())
for i in range(t):
    n = int(input())
    dp = [1]*101
    for j in range(4,n+1):
        dp[j] = dp[j-2]+dp[j-3]
    print(dp[n])