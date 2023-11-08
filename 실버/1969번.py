n,m = map(int,input().split())
dna = [list(input()) for _ in range(n)]

s = []
for i in range(m):
    cnt = {'A':0,'T':0,'C':0,'G':0}
    for j in range(n):
        cnt[dna[j][i]] += 1

    x = [k for k,v in cnt.items() if max(cnt.values()) == v]
            
    if len(x) > 1:
        x = sorted(x)[0]

    s.append(*x)

s = ''.join(s)
ans = 0
for v in dna:
    for j in range(m):
        if s[j] != v[j]:
            ans += 1

print(s)
print(ans)