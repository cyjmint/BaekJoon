n = int(input())
nums = list(map(int,input().split()))
order = [1]*n

for i in range(n):
    for j in range(i):
        if nums[j] > nums[i]:
            order[i] = max(order[i], order[j]+1)

print(max(order))