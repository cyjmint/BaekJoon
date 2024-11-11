n = int(input())
score = [0] * 300
dp = [0] * 300 #n번째 계단을 밟았을 때 최댓값
for i in range(n):
    score[i] = int(input())

dp[0] = score[0]
dp[1] = max(score[0]+score[1], score[1])
dp[2] = max(score[0]+score[2], score[1]+score[2])

for i in range(3,n):
    dp[i] = max(score[i]+dp[i-2], score[i]+score[i-1]+dp[i-3])
    #마지막 계단을 기준으로 전 계단을 밟았을 때, 전전 계단을 밟았을 때 두 가지 경우를 생각
    #전 계단을 밟았을 경우에는 연속해서 세 계단을 밟지 못하므로 n-3번째 계단을 밟고 와야 함
    #n-3이 음수가 되면 안되므로 초기값을 3개 설정해야 함
print(dp[n-1])
