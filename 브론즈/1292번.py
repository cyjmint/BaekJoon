A,B = list(map(int,input().split()))
n = []
a = 1
while len(n) <= B:
    num = [a]*a
    n.extend(num)
    a += 1
print(sum(n[(A-1):B]))