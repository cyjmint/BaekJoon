N = int(input())
num = list(map(int,input().split()))

n = 0
for value in num:
    f = []
    for i in range(1,value+1):
        if value % i == 0:
            f.append(i)
    if len(f) == 2:
        n += 1
        
print(n)

