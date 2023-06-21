N = int(input())
for i in range(N):
    a = input()
    b = list(a)
    n = []
    if b[0] == 'O':
        n.insert(0,1)
    else:
        n.insert(0,0)
    for j in range(1,len(b)):
        if b[j] == 'O':
            n.insert(j,1 + n[j-1])
        else:
            n.insert(j,0)
    print(sum(n))