#Memoization 방식 (Top-down)
l = [] 
for _ in range(21):
    l.append([[' ']*21 for _ in range(21)])

def w(a,b,c):
    if a<=0 or b<=0 or c<=0:
        a = 0; b = 0; c = 0
    else:
        if a>20 or b>20 or c>20:
            a = 20; b = 20; c = 20
            
    if l[a][b][c] != ' ':
        return l[a][b][c]
    else:
        if a == 0 or b == 0 or c == 0:
            l[a][b][c] = 1
        else:
            if a<b and b<c:
                l[a][b][c] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
            else:
                l[a][b][c] = w(a-1,b,c) + w(a-1,b-1,c) + w(a-1,b,c-1) - w(a-1,b-1,c-1)
        return l[a][b][c]
        
        
while True:
    a,b,c = map(int,input().split())
    if a == -1 and b == -1 and c == -1:
        break
    else:
        print(f'w({a}, {b}, {c}) = {w(a,b,c)}')

#%%
#Tabulation 방식 (Bottom-up)
l = []
for _ in range(21):
    l.append([[' ']*21 for _ in range(21)])

def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        a = 0; b = 0; c = 0
    if a > 20 or b > 20 or c > 20:
        a = 20; b = 20; c = 20
        
    for i in range(a+1):
        for j in range(b+1):
            for z in range(c+1):
                if i == 0 or j == 0 or z == 0:
                    if l[i][j][z] == ' ':
                        l[i][j][z] = 1
                    else:
                        pass
                else:
                    if i < j and j < z:
                        if l[i][j][z] == ' ':
                            l[i][j][z] = l[i][j][z-1] + l[i][j-1][z-1] - l[i][j-1][z]
                        else:
                            pass
                    else:
                        if l[i][j][z] == ' ':
                            l[i][j][z] = l[i-1][j][z] + l[i-1][j-1][z] + l[i-1][j][z-1] - l[i-1][j-1][z-1]
                        else:
                            pass
                        
    return l[a][b][c]

while True:
    a,b,c = map(int,input().split())
    if a == -1 and b == -1 and c == -1:
        break
    else:
        print(f'w({a}, {b}, {c}) = {w(a,b,c)}')