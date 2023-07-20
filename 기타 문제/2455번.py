n = 0
num = []
for i in range(4):
    a,b = list(map(int,input().split()))
    n += (b-a)
    num.append(n)
print(max(num))