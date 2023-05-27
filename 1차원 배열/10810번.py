#import sys
#input = sys.stdin.readline
N, M = list(map(int,input().split()))
data = [0]*N
for a in range(M):
    i, j, k = list(map(int, input().split()))
    for b in range(i-1,j):
        data[b] = k
for c in range(len(data)):
    print(data[c], end = ' ')