T = int(input())
sums = []
for i in range(0,T):
    A, B = list(map(int,input().split()))
    s = A + B
    sums.append(s)
for j in sums:
    print(j)
