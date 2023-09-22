x = list(map(int,input().split()))
y = list(map(int,input().split()))
s = sum(x); t = sum(y)
if s >= t:
    print(s)
else:
    print(t)