num = [1, 1, 2, 2, 2, 8]
N = list(map(int,input().split()))
for i in range(len(num)):
    print(num[i] - N[i], end = ' ')