n = int(input())
time = list(map(int,input().split()))

y = []; m = []
for t in time:
    y.append(10*((t//30)+1))
    m.append(15*((t//60)+1))

if sum(y) < sum(m):
    print('Y',sum(y))
if sum(m) < sum(y):
    print('M',sum(m))
if sum(m) == sum(y):
    print('Y','M',sum(y))