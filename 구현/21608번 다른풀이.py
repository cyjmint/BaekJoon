#좌표 이동할 때 사용하는 리스트
#상하좌우로만 이동할 수 있기 때문에, 행 방향으로 이동할 떄는 열 방향으로 못 움직이고, 그 반대도 똑같음.
dr = [-1, 1, 0, 0] #행
dc = [0, 0, -1, 1] #열

n = int(input())
arr = [[0]*n for _ in range(n)] #교실 자리
## 한 번에 정보를 받음
students = [list(map(int, input().split())) for _ in range(n**2)] #학생 + 해당 학생이 좋아하는 학생들 정보

## 학생 수 만큼 for문을 돌며 자리에 앉혀 줌.
for order in range(n**2):
    student = students[order]
    ## 여기다가 가능한 자리를 다 담아서 정렬 후 앉힘
    tmp = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0: #자리에 학생이 없다면,
                like = 0
                blank = 0
                for k in range(4):
                    nr, nc = i + dr[k], j + dc[k] #좌표 수정
                    if 0 <= nr < n and 0 <= nc < n: 
                        if arr[nr][nc] in student[1:]:
                            like += 1
                        if arr[nr][nc] == 0:
                            blank += 1
                tmp.append([like, blank, i, j])
    ### !!!! like, blank는 클 수록, 행과 열의 수는 작을수록 답이니 lambda 뒤의 조건을 잘 줘야함!!!
    tmp.sort(key= lambda x:(-x[0], -x[1], x[2], x[3]))
    #1. like를 기준으로 내림차순으로 정렬
    #2. 위에서 정렬된 순서를 유지하며, blank를 기준으로 내림차순으로 정렬
    #3. 위에서 정렬된 순서를 유지하며, 행을 기준으로 오름차순으로 정렬
    #4. 위에서 정렬된 순서를 유지하며, 열을 기준으로 오름차순으로 정렬

    ### 정렬 후 젤 앞에 있는 리스트의 행과 열의 번호에 학생 앉히기 
    arr[tmp[0][2]][tmp[0][3]] = student[0]

result = 0
## 점수를 매길 때는 학생 순서대로 점수 주기 위해 정렬함 
students.sort()

for i in range(n):
    for j in range(n):
        ans = 0
        for k in range(4):
            nr, nc = i + dr[k], j + dc[k]
            if 0 <= nr < n and 0 <= nc < n:
                if arr[nr][nc] in students[arr[i][j]-1]:
                    ans += 1
        if ans != 0:
            result += 10 ** (ans-1)
print(result)