import sys
from collections import deque
input = sys.stdin.readline

def bfs(i, j, building = 0):
    move = [(0,0),(1,0),(-1,0),(0,1),(0,-1)] # 시작 인덱스부터 집이 있는지 확인해야 함
    queue = deque([(i,j)])
    num = 0

    while queue:
        x,y = queue.popleft()

        for a,b in move:
            nx = x + a; ny = y + b
            if 0 <= nx < N and 0 <= ny < N and house[nx][ny] != '0':
                num += 1
                house[nx][ny] = '0'
                queue.append((nx,ny))
    #더 이상 인접한 건물이 없다면, 단지 한 개 확인한 것
    building += 1
    num_house.append(num)

    return building

N = int(input())
house = [list(input().rstrip()) for _ in range(N)]
num_house = []
building = 0
for i in range(N):
    for j in range(N):
        if house[i][j] == '1':
            building = bfs(i,j,building)

print(building)
for i in range(building):
    print(sorted(num_house)[i])