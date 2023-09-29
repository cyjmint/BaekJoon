f = []
num = 0
def fib(n):
    global num
    f.append(1)
    f.append(1)
    for i in range(2,n):
        f.append(f[i-1]+f[i-2])
        num+=1
    return f[n-1]

n = int(input())
print(fib(n), end = ' ')
print(num)