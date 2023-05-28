#import sys
#input = sys.stdin.readline

N, M = list(map(int, input().split()))
data = []
for a in range(N):
    data.append(a+1)
for b in range(M):
    i, j = list(map(int, input().split()))
    data2 = list(reversed(data[i-1:j]))
    data[i-1:j] = data2[0:j-i+1]
for c in range(len(data)):
    print(data[c], end = ' ')