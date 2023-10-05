n = int(input())
price = []
for _ in range(n):
    a,b,c = map(int,input().split())
    if a==b==c:
        price.append(1000*a + 10000)
    if a!=b!=c:
        price.append(max([a,b,c])*100)
    if a==b and a!=c:
        price.append(100*a + 1000)
    if a==c and a!=b:
        price.append(100*a + 1000)
    if b==c and b!=a:
        price.append(100*b + 1000)

print(max(price))