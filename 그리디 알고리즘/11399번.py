n = int(input())
p = list(map(int,input().split()))
p = sorted(p)
times = []

for i in range(n):
    for j in range(0,i+1):
        time = 0
        time += p[j]
        times.append(time)

print(sum(times))