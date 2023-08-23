from collections import Counter

n = int(input())
num = [int(input()) for _ in range(n)]
num.sort()

dic = Counter(num)

f = [k for k,v in dic.items() if v == max(dic.values())]
a = f[0] if len(f) == 1 else f[1]

print(round(sum(num)/n))
print(num[(n+1)//2-1])
print(a)
print(num[-1] - num[0])