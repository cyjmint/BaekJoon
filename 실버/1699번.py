n = int(input())
l = [0 for _ in range(n+1)]
psn = []
psn.append(1); l[1] = 1

def is_psn(n):
    if n**.5 - int(n**.5) == 0.0:
        return True
    return False

def sum_psn(n):
    for i in range(2,n+1):
        if is_psn(i):
            l[i] = 1
            psn.append(i)
        else:
            sub = []
            for num in psn:
                sub.append(l[num]+l[i-num])
            l[i] = min(sub)
    return l[n]

if n == 1:
    print(1)
else:
    print(sum_psn(n))