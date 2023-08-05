n = int(input())
y = [0]*(n+1)
for i in range(n+1):
    if i == 0:
        y[i] = 0
    elif i == 1:
        y[i] = 1
    else:
        y[i] = y[i-1] + y[i-2]
print(y[-1])