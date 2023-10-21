k = int(input())
a = [0]*k; b = [0]*k
a[0] = 0; b[0] = 1

for i in range(1,k):
    if i == 1:
        a[i] = 1; b[i] = 1
    else:
        a[i] = a[i-1]+a[i-2]
        b[i] = b[i-1]+b[i-2]

print(a[-1],b[-1])