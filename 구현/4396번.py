n = int(input())
mine = [list(input()) for _ in range(n)]
click = [list(input()) for _ in range(n)]
ans = [['.']*n for _ in range(n)]

#상하좌우 대각선 이동할 때 쓸 리스트
dr = [1,-1,0,0,1,-1,1,-1]
dc = [0,0,1,-1,1,-1,-1,1]

r = []; c = [] #지뢰가 있는 곳의 좌표
for i in range(n):
    for j in range(n):
        if mine[i][j] == '*':
            r.append(i); c.append(j)

for i in range(n):
    for j in range(n):
        num = 0 #인접한 8개의 칸에 있는 지뢰의 개수

        if click[i][j] == 'x': #열린 칸이고
            if mine[i][j] == '.': #지뢰가 없으면

                for z in range(8):
                    a = i+dr[z]; b = j+dc[z] #상하좌우 대각선 이동
                    if a < 0 or b < 0 or a >= n or b >= n: #이동했는데 범위를 벗어나면 되돌아가기
                        continue
                    if mine[a][b] == '*': #인접한 8개의 칸에 지뢰가 있다면
                        num += 1
                ans[i][j] = num

            else: #지뢰가 있으면
                for z in range(len(r)):
                    ans[r[z]][c[z]] = '*' #지뢰가 있는 모든 칸을 표시

for i,row in enumerate(ans):
    for j,result in enumerate(row):
        print(result, end = '')
    print()