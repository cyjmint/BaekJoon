def power(a,b,c):
    if b == 1:
        return a%c
    else:
        x = power(a,b//2,c)
        if b%2 == 0:
            return x*x%c
        else:
            return x*x*a%c

a,b,c = map(int,input().split())
print(power(a,b,c))