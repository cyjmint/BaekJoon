seq = []
def backtrack(n,m):
    seq2 = sorted(seq)
    if len(seq) == m and seq2 == seq:
        print(' '.join(map(str,seq)))
        return
    else:
        for i in range(1,n+1):
            if i not in seq:
                seq.append(i)
                backtrack(n,m)
                seq.pop()
                
n,m = map(int,input().split())
backtrack(n,m)