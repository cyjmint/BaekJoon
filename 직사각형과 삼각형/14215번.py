a,b,c = list(map(int,input().split()))
if max(a,b,c) < a+b+c-max(a,b,c):
    print(a+b+c)
else:
    n = max(a,b,c)
    while n >= a+b+c-max(a,b,c):
        n = n - 1
    print(a+b+c-max(a,b,c)+n)