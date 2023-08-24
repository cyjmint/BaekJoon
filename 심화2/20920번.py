from collections import Counter

n,m = map(int,input().split())
words = [input() for _ in range(n)]

frequency = Counter(words)
keys = list(frequency.keys())
for k in keys:
    if len(k) < m:
        del frequency[k]
        
n = max(frequency.values())
while n > 0:
    a = []
    for k,v in frequency.items():
        if v == n:
            a.append(k)
    if len(a) > 1:
        a = sorted(a)
        a = sorted(a,key=len,reverse=True)
    for v in a:
        print(v)
    n -= 1