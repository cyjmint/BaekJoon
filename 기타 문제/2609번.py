a,b = list(map(int,input().split()))
n = 1
x = []
while n <= min(a,b):
    if a%n==0 and b%n==0:
        x.append(n)
        n+=1
    else:
        n+=1
print(max(x))
print(max(x)*(a//max(x))*(b//max(x)))