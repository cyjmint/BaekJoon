N, M = map(int,input().split())
num = list(map(int,input().split()))

s = []
for i in range(N-2):
    for j in range(i+1, N-1):
        for z in range(j+1, N):
            a = num[i] + num[j] + num[z]
            if a <=  M:
                s.append(a)
                
print(max(s))