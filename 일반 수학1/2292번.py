N = int(input())

n = 0
while True:
    if (1+3*n*(n+1)) < N and N <= (1+3*(n+1)*(n+2)):
        break
    else:
        n += 1
    if N == 1:
        n = -1
        break
    
print(n+2)
        
