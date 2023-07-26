N = int(input())
n = []

for x in range((N//5)+1):
    if (N-5*x)%3 == 0:
        y = (N-5*x)//3    
        n.append(x+y)

if len(n) == 0:
    print(-1)
else:
    print(min(n))