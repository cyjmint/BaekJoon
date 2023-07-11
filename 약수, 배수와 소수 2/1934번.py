T = int(input())
for i in range(T):
    A,B = list(map(int,input().split()))
    num = [x for x in range(1,max(A,B)+1) if A%x == 0 and B%x == 0]
    print((A*B)//num[-1])