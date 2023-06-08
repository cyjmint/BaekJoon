from string import ascii_uppercase
alp = list(ascii_uppercase)
num = [i for i in range(10,36)]

N, B = list(map(int,input().split()))

l = []
while N > 0:
    L = N%B
    N = N//B
    l.append(L)

l = list(reversed(l))
for i in range(len(l)):
    for j in range(len(num)):
        if l[i] == num[j]:
            l[i] = alp[j]
        else:
            pass
    print(l[i], end = '')

