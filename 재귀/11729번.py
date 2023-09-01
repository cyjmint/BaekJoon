n = int(input())
k = []
def hanoi(n,start,by,end):
    if n == 1:
        k.append([start, end])
    else:
        hanoi(n-1,start,end,by)
        k.append([start, end])
        hanoi(n-1,by,start,end)

hanoi(n, '1', '2', '3')
print(len(k))
for v in k:
    print(*v)