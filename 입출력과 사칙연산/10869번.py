## 10869번 문제

import math

A, B = map(int, input().split())
if A in list(range(1, 10001)) and B in list(range(1, 10001)):
    print(A+B)
    print(A-B)
    print(A*B)
    print(math.trunc(A/B))
    print(A%B)
else:
    pass
    
    

