n = int(input())
score = [int(input()) for _ in range(n)]
ans = 0

for i in range(1,n):
    a = score[-i]; b = score[-i-1]
    if a <= b:
        ans += b-a+1
        score[-i-1] -= b-a+1

print(ans)