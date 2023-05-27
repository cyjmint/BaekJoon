#import = sys
#input = sys.stdin.readline
N, M = list(map(int,input().split()))
data = []
x = 1
while x <= N:
    data.append(x)
    x += 1
for a in range(M):
    i, j = list(map(int,input().split()))
    b = data[i-1]
    c = data[j-1]
    data[i-1] = c
    data[j-1] = b
for d in range(len(data)):
    print(data[d], end = ' ')