def fac(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fac(n-1)

n = int(input())
num = list(str(fac(n)))
ans = 0
while True:
    if num.pop(-1) == '0':
        ans += 1
    else:
        break

print(ans)