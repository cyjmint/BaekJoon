def lotto(num):
    if nums != sorted(nums):
        return
    if len(nums) == 6 and nums == sorted(nums):
        print(*nums)
        return
    for v in num:
        if v not in nums:
            nums.append(v)
            lotto(num)
            nums.pop()

while True:
    n = list(map(int,input().split()))
    if n == [0]:
        break
    k = n[0]; num = [n[i] for i in range(1,k+1)]; nums = []
    lotto(num)
    print()