n = int(input())
classroom = [[0]*n for _ in range(n)] #학생의 자리
student = []; like = [] #학생과 각 학생이 좋아하는 학생
for _ in range(n**2):
    l = list(map(int,input().split()))
    student.append(l[0])
    l.pop(0)
    like.append(l)

for x in range(n**2): #자리를 정할 학생들
    place = [] #자리 후보
    num_place = []
    empty_place = []

    for r,row in enumerate(classroom): #행
        for c,value in enumerate(row): #열
            if classroom[r][c] == 0: #비어있는 자리에 중에서

                num = 0 #좋아하는 학생이 있는 인접한 자리의 수
                empty = 0 #비어있는 인접한 자리의 수

                if 0 < r <= n-2:
                    if classroom[r-1][c] in like[x]: #인접한 자리에 좋아하는 학생이 있으면
                        num += 1
                    if classroom[r+1][c] in like[x]: #인접한 자리에 좋아하는 학생이 있으면
                        num += 1
                    if classroom[r-1][c] == 0: #인접한 자리가 비어 있으면
                        empty += 1
                    if classroom[r+1][c] == 0: #인접한 자리가 비어 있으면
                        empty += 1
                    
                if 0 < c <= n-2:
                    if classroom[r][c-1] in like[x]: #인접한 자리에 좋아하는 학생이 있으면
                        num += 1
                    if classroom[r][c+1] in like[x]: #인접한 자리에 좋아하는 학생이 있으면
                        num += 1
                    if classroom[r][c-1] == 0: #인접한 자리가 비어 있으면
                        empty += 1
                    if classroom[r][c+1] == 0: #인접한 자리가 비어 있으면
                        empty += 1

                if r == 0: #첫번째 행에 있는 자리
                    if classroom[r+1][c] in like[x]: #인접한 자리에 좋아하는 학생이 있으면
                        num += 1
                    if classroom[r+1][c] == 0: #인접한 자리가 비어 있으면
                        empty += 1

                if c == 0: #첫번째 열에 있는 자리
                    if classroom[r][c+1] in like[x]: #인접한 자리에 좋아하는 학생이 있으면
                        num += 1
                    if classroom[r][c+1] == 0: #인접한 자리가 비어 있으면
                        empty += 1

                if r == n-1: #마지막 행에 있는 자리
                    if classroom[r-1][c] in like[x]: #인접한 자리에 좋아하는 학생이 있으면
                        num += 1
                    if classroom[r-1][c] == 0: #인접한 자리가 비어 있으면
                        empty += 1

                if c == n-1: #마지막 열에 있는 자리
                    if classroom[r][c-1] in like[x]: #인접한 자리에 좋아하는 학생이 있으면
                        num += 1
                    if classroom[r][c-1] == 0: #인접한 자리가 비어 있으면
                        empty += 1

                place.append([r,c])
                num_place.append(num)
                empty_place.append(empty)
    
    #조건 1
    np = [] #좋아하는 학생이 인접한 자리에 가장 많은 자리
    m = max(num_place)
    for i,v in enumerate(num_place):
        if v == m:
            np.append(i)

    if len(np) == 1:
        i = np[0]
        classroom[place[i][0]][place[i][1]] = student[x]

    else:
        #조건 2
        l = [empty_place[i] for i in np] #조건 1을 만족하는 자리 
        ep = [] #인접한 자리 중에 비어있는 자리가 가장 많은 자리
        m = max(l)
        for i,v in enumerate(l):
            if v == m:
                ep.append(np[i])

        if len(ep) == 1:
            i = ep[0]
            classroom[place[i][0]][place[i][1]] = student[x]
            
        else:
            #조건 3
            place2 = [place[i] for i in ep] #조건 1과 2를 만족하는 자리
            place2 = sorted(place2) #행의 번호를 오름차순 정렬한 후, 열의 번호를 오름차순 정렬
            classroom[place2[0][0]][place2[0][1]] = student[x]
            i = place.index(place2[0])

ans = 0 #만족도
for r,row in enumerate(classroom): #행
        for c,v in enumerate(row): #열
            num = 0 #좋아하는 학생이 있는 인접한 자리의 수
            i = student.index(v)
            
            if 0 < r <= n-2:
                if classroom[r-1][c] in like[i]: #인접한 자리에 좋아하는 학생이 있으면
                    num += 1
                if classroom[r+1][c] in like[i]: #인접한 자리에 좋아하는 학생이 있으면
                    num += 1
                    
            if 0 < c <= n-2:
                if classroom[r][c-1] in like[i]: #인접한 자리에 좋아하는 학생이 있으면
                    num += 1
                if classroom[r][c+1] in like[i]: #인접한 자리에 좋아하는 학생이 있으면
                    num += 1

            if r == 0: #첫번째 행에 있는 자리
                if classroom[r+1][c] in like[i]: #인접한 자리에 좋아하는 학생이 있으면
                    num += 1

            if c == 0: #첫번째 열에 있는 자리
                if classroom[r][c+1] in like[i]: #인접한 자리에 좋아하는 학생이 있으면
                    num += 1
                    
            if r == n-1: #마지막 행에 있는 자리
                if classroom[r-1][c] in like[i]: #인접한 자리에 좋아하는 학생이 있으면
                    num += 1

            if c == n-1: #마지막 열에 있는 자리
                if classroom[r][c-1] in like[i]: #인접한 자리에 좋아하는 학생이 있으면
                    num += 1

            if num == 1:
                ans += 1
            if num == 2:
                ans += 10
            if num == 3:
                ans += 100
            if num == 4:
                ans += 1000

print(ans)