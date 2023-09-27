seq = []
def backtracking(n,m):
    if len(seq) == m:
        print(' '.join(map(str,seq)))
        return
    else:
        for i in range(1,n+1):
            seq.append(i)
            backtracking(n, m)
            seq.pop()

n,m = map(int,input().split())
backtracking(n, m)