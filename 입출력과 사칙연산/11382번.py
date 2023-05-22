A, B, C = list(map(int,input().split()))
r = range(1,10**12+1)
if A in r and B in r and C in r:
    print(A + B + C)
    