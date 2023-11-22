n = int(input())
dp = [[0]*10 for _ in range(n+1)]
dp[1] = [0,1,1,1,1,1,1,1,1,1]
#dp[i][j]에서 i는 자릿수, j는 마지막 자리의 숫자

for i in range(2,n+1):
    dp[i][0] = dp[i-1][1] #0과 1 차이 나는 자연수는 1 밖에 없다
    dp[i][9] = dp[i-1][8] #9와 1 차이 나는 자연수는 8 밖에 없다
    for j in range(1,9):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1] #나머지 수들은 1 차이 나는 수가 2개 있다

print(sum(dp[n])%int(1e9))