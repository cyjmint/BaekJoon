N = int(input())
a = list(map(int,input().split()))
B,C = list(map(int,input().split()))

n = 0
for i in range(N):
    x = (a[i]-B)
    if x <= 0:
        n += 1
    elif x/C < 1:
        n += 2
    elif x%C != 0:
        n += x//C+2
    else:
        n += x//C+1
        
print(n)