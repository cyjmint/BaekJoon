import sys
input = sys.stdin.readline

T = int(input())
# 행 : n, 열 : 1 또는 2 또는 3으로 시작하는 연산의 가짓수
dp = [[0] * 4 for _ in range(100001)]
dp[1][1] = 1; dp[1][2] = 0; dp[1][3] = 0
dp[2][1] = 0; dp[2][2] = 1; dp[2][3] = 0
dp[3][1] = 1; dp[3][2] = 1; dp[3][3] = 1
ans = [0] * 100001
# 이전에 계산한 값들을 저장해 다시 계산하지 않도록 함
ans[1] = 1; ans[2] = 1; ans[3] = 3

for j in range(T):
    n = int(input())

    if ans[n] != 0:
        print(ans[n])
        continue

    for i in range(4,n+1):
        if ans[n] == 0:
            dp[i][1] = (dp[i-1][2] + dp[i-1][3]) % 1000000009
            dp[i][2] = (dp[i-2][1] + dp[i-2][3]) % 1000000009
            dp[i][3] = (dp[i-3][1] + dp[i-3][2]) % 1000000009
            ans[i] = (dp[i][1] + dp[i][2] + dp[i][3]) % 1000000009

    print(ans[n])