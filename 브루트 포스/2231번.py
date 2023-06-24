N = int(input())
M = 0
while True:
    l = list(map(int,list(str(M))))
    if N != M + sum(l):
        M += 1
    else:
        print(M)
        break
    if M > N:
        print(0)
        break