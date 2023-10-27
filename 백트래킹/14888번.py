n = int(input())
nums = list(map(int,input().split()))
add,sub,mul,div = map(int,input().split())

max_result = -1e10; min_result = 1e10

def f(i,result):
    global max_result, min_result, add, sub, mul, div
    if i == n:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
    else:
        if add > 0:
            add -= 1
            f(i+1, result + nums[i])
            add += 1
        if sub > 0:
            sub -= 1
            f(i+1, result - nums[i])
            sub += 1
        if mul > 0:
            mul -= 1
            f(i+1, result * nums[i])
            mul += 1
        if div > 0:
            div -= 1
            f(i+1, int(result / nums[i]))
            div += 1

f(1,nums[0])
print(max_result)
print(min_result)