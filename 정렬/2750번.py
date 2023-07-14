N = int(input())
num = []
for i in range(N):
    num.append(int(input()))

n = N
while n > 0:
    for i in range(N-1):
        if num[i] > num[i+1]:
            num[i], num[i+1] = num[i+1], num[i]
    n -= 1
print(num)