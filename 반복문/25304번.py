X = int(input())
N = int(input())
if N not in range(1, 101) or X not in range(1, (10**9)+1):
    pass
else:
    prices = []
    for i in range(0,N):
        a, b = list(map(int,input().split()))
        if a not in range(1, (10**6)+1) or b not in range(1,11):
            break
        prices.append(a*b)
    else:
        if sum(prices) == X:
            print('Yes')
        else:
            print('No')



X = int(input())
N = int(input())
prices = []
for i in range(0,N):
    a, b = list(map(int,input().split()))
    prices.append(a*b)
if sum(prices) == X:
    print('Yes')
else:
    print('No')
        
 
