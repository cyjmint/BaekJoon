num = []
x = []
y = []
for i in range(3):
    num.append(list(map(int,input().split())))
    x.append(num[i][0])
    y.append(num[i][1])
    
for i in range(len(x)):
    if x.count(x[i]) != 2:
        a=x[i]
    if y.count(y[i]) != 2:
        b=y[i]
print(a, end = ' ')
print(b)