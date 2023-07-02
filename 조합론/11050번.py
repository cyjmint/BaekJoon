N,K = list(map(int,input().split()))
n=1
for i in range(N-K+1,N+1):
    n*=i
k=1
for i in range(1,K+1):
    k*=i
print(int(n/k))