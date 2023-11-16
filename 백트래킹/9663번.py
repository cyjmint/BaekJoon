n = int(input())
col = [0]*n
ans = 0

def promising(i):
    for k in range(i):
        if col[i] == col[k] or abs(i-k) == abs(col[i]-col[k]):
            return False

    return True

def nqueen(i):
    global ans
    if i == n:
        ans += 1
        return
        
    else:
        for j in range(n):
            col[i] = j
            if i > 0:
                if abs(col[i-1]-col[i]) < 2:
                    continue
            if promising(i):
                nqueen(i+1)

nqueen(0)
print(ans)