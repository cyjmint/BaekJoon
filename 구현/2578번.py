bingo = [list(map(int,input().split())) for _ in range(5)]
call = []
for _ in range(5):
    n = map(int,input().split())
    for _ in range(5):
        call.append(next(n))

rsum = []; csum = []; dsum = [] #행,열,대각선의 합
ds1 = 0; ds2 = 0 #ds1 : 행과 열의 인덱스가 같을 때 대각선, ds2 : 행과 열의 인덱스의 합이 4일 때 대각선
for i in range(5):
    rsum.append(sum(bingo[i]))
    cs = 0
    for j in range(5):
        cs += bingo[j][i]
        if i == j:
            ds1 += bingo[i][j]
        if i+j == 4:
            ds2 += bingo[i][j]
    csum.append(cs)
dsum.append(ds1)
dsum.append(ds2)

line = 0 #line : 선이 몇개 그어졌는지
for i in range(len(call)): #사회자가 부르는 수의 좌표
        
        if line >= 3: #빙고가 되었을 때
            print(i) #몇 번째 수인가
            break

        x = 0; y = 0 #빙고판에 있는 수의 좌표
        check = 1 #사회자가 부른 수와 빙고판에 있는 수가 같은지 체크. 같으면 0, 다르면 1
            
        while check:
            if call[i] == bingo[x][y]:
                rsum[x] -= bingo[x][y]
                csum[y] -= bingo[x][y]
                if x == y:
                    dsum[0] -= bingo[x][y]
                if x+y == 4:
                    dsum[1] -= bingo[x][y]
                bingo[x][y] = 0
                check = 0
                if rsum[x] == 0: #행의 합이 0 : 행의 모든 수가 체크 됨
                    line += 1
                if csum[y] == 0: #열의 합이 0 : 열의 모든 수가 체크 됨
                    line += 1
                if x == y and dsum[0] == 0: #대각선의 합이 0
                    line += 1
                if x+y == 4 and dsum[1] == 0: #대각선의 합이 0
                    line += 1

            else: #빙고판 좌표 이동
                if y != 4:
                    y += 1
                    continue
                if x != 4 and y == 4:
                    x += 1
                    y = 0  