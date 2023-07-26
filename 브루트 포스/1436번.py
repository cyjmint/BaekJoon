N = int(input())
a = 666
num = []

while len(num) < N:
    A1 = list(reversed(str(a)))
    A2 = len(str(a))
    n = []; s=[]
    for i in range(A2):
        if A1[i] == '6':
            n.append(i)
    for j in range(len(n)-2):
        if n[j]+1 == n[j+1] and n[j+1]+1 == n[j+2]:
            s.append(n[j])
    if max(s)+2 == max(n) or max(n) == A2:
        i = max(n)
    else:
        i = max(s)+2
    b = a//10**(i-2) * 10**(i-2)
    for j in range(10**(i-2)):
        c = b+j
        num.append(c)
    a += 1000

print(sorted(num)[N-1])