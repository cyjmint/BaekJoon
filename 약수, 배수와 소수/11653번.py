N = int(input())

for n in range(2,N+1):
    if N%n == 0:
        while N%n < 1:
            N = N//n
            print(n)
