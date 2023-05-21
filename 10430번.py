A, B, C = list(map(int, input().split()))
r = list(range(1,10001))
def remainder(A,B,C):
    if A in r and B in r and C in r:
        print((A+B)%C),
        print(((A%C)+(B%C))%C),
        print((A*B)%C),
        print(((A%C)*(B%C))%C)
    return
    
remainder(A,B,C)
