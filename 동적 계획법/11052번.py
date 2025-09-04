import sys
input = sys.stdin.readline

N = int(input())
P = [int(i) for i in list(input().split())]

# dp(1) : P1
# dp(2) : P2 or P1*2 = P2 or dp(1)+dp(1)
# dp(3) : P3 or P2+P1 or P1*3 = P3 or dp(2)+dp(1)
# dp(4) : P4 or P3+P1 or P2+P1+P1 or P2*2 or P1*4 = P4 or dp(3)+dp(1) or dp(2)+dp(2)
# dp(5) : P5 or P4+P1 or P3+P2 or P3+P1*2 or P2+P1*3 or P2*2+P1 or P1*5 = P5 or dp(4)+dp(1) or dp(3)+dp(2)

dp = [0]*N
dp[0] = P[0]
dp[1] = max(P[1], dp[0]*2)
for i in range(2, N):
    for j in range(i//2+1):
        dp[i] = max(P[i], dp[j]+dp[i-1-j], dp[i])

print(dp[-1])