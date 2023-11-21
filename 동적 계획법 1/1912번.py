n = int(input())
seq = list(map(int,input().split()))
dp = [0]*n #연속합을 저장
dp[0] = seq[0] #1번째까지의 연속합
ans = seq[0] #1번째까지의 최대 연속합
             #현재 최대 연속합을 저장

for i in range(1,n):
    dp[i] = max(dp[i-1]+seq[i],seq[i]) #i번째까지의 연속합 : i-1번째까지의 연속합 + 수열의 i번째 값
                                       #max(i-1번째까지의 연속합 + 수열의 i번째 값, 수열의 i번째 값) : 만약 수열의 i번째 값이 더 크다면, 연속이 끊어졌다는 의미. i-1번째까지의 연속합을 더 계산하는 것은 손해.
    ans = max(ans,dp[i]) #지금까지의 전체 연속합의 최댓값(ans)과 i번째까지의 연속합(dp[i]) 중에 더 큰 값이 현재 최대 연속합

print(ans)