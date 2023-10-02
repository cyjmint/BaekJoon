n = int(input())
f = int(input())

x = n%100

if x == 0:
    for i in range(n,n+100):
        if i%f == 0:
            y = i%100
            break
else:
    for i in range(n-x,n-x+100):
        if i%f == 0:
            y = i%100
            break

if y < 10:
    print('0'+str(y))
else:
    print(y)