from itertools import permutations

n = int(input())
arr = list(map(int,input().split()))
nums = list(permutations(arr,n))
ans = 0
for i in range(len(nums)):
    total = 0
    for j in range(n-1):
        total += abs(nums[i][j]-nums[i][j+1])
        ans = max(total, ans)

print(ans)