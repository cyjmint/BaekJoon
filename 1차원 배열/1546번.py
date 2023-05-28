N = int(input())
data = list(map(int,input().split()))
M = max(data)

data2 = []
for i in range(len(data)):
    data2.append((data[i]/M)*100)
data2_m = sum(data2)/N
print(data2_m)
