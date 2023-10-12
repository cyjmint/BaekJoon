exp = input().split('-')
sums = []
for v in exp:
    num = list(map(int,v.split('+')))
    sums.append(sum(num))
a = sums.pop(0)
b = sum(sums)
print(a-b)