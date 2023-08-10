T = int(input())
num = []
for i in range(T):
    num.append(int(input()))

n = max(num)
x = n//2
l = [0]*(n+1)
for j in range(2,int(n**.5)+1):
    if l[j] == 0:
        k = j
        while j*k <= n:
            l[j*k] = 1
            k += 1

for v in num:
    z = 0
    for m in range(2,v//2+1):
        if l[m] == 0:
            y = v-m
            if l[y] == 0:
                z += 1
    print(z)