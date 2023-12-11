N,M,K = map(int,input().split())
n = K//M
m = K%M
print(n,m)

#크기가 NxM인 모눈에서 좌표 (n,m)의 순서가 k번째라면, n = k//M, m = k%M