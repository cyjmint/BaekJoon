#사각형이 겹친 문제를 풀 때는 겹친 부분의 넓이를 빼는 것보다, 
#이차원 배열로 좌표를 만든 다음 하나씩 색칠하가면서 이미 색칠된 부분은 건너뛰는 방식으로 하는 것이 더 간단함
square = [[0]*101 for _ in range(101)]
ans = 0
for _ in range(4):
    a,b,c,d = map(int,input().split())
    for i in range(a,c): #좌표의 마지막은 포함시키면 안됨
        for j in range(b,d):
            if square[i][j] == 0:
                square[i][j] = 1
                ans += 1

print(ans)