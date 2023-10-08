n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

num = []
for i in range(n):
    num.append(max(b)*min(a))
    a.pop(a.index(min(a)))
    b.pop(b.index(max(b)))

print(sum(num))