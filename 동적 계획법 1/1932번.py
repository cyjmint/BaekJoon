n = int(input())
nums = [list(map(int,input().split())) for _ in range(n)]

for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            nums[i][j] += nums[i-1][j]
        if j == i:
            nums[i][j] += nums[i-1][j-1]
        if j != 0 and j != i:
            nums[i][j] += max(nums[i-1][j],nums[i-1][j-1])

print(max(nums[n-1]))