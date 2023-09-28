seq = []
def backtracking(start):
    if len(seq) == m:
        print(' '.join(map(str,seq)))
        return
    else:
        for i in range(start,n+1):
            seq.append(i)
            backtracking(i)
            seq.pop()
      
n,m = map(int,input().split())
backtracking(1)