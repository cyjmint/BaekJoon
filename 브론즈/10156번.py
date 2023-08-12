k,n,m = list(map(int,input().split()))
if k*n >= m:
    print(k*n-m)
else:
    print(0)