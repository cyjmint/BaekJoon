m = int(input())
list = [1,2,3]
for _ in range(m):
    x,y = map(int,input().split())
    i = list.index(x); j = list.index(y)
    list[i] = y; list[j] = x

print(list[0])