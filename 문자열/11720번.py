N = int(input())
S = input()
if len(S) != N:
    pass
else:
    s = 0
    num = list(S)
    for i in range(N):
        s += int(num[i])
    print(s)
    