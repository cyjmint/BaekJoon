import sys
input = sys.stdin.readline

N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

# 얼음이 있는 좌표
ice = {}
for i in range(1,N-1):
    for j in range(1,M-1):
        if graph[i][j] != 0:
            ice[(i,j)] = 1

dx = [0,0,1,-1]
dy = [1,-1,0,0]

# 빙산의 덩어리를 판단하는 기준 -> dfs 사이클 수 = 빙산의 덩어리 수
# dfs를 실행하면서 얼음을 만나면 stack에 추가 -> dfs 한 사이클이 돌면 빙산 덩어리 하나가 있는 것

def dfs(start):
    x,y = start
    linked_ice = [(x,y)]

    # 주변에 얼음이 없으면 함수 종료 -> 빙산의 덩어리 1개가 있다는 의미
    while linked_ice:
        x,y = linked_ice.pop()
        if not visited_ice[x][y]: # 방문하지 않은 얼음인 경우에만 진행
            visited_ice[x][y] = True

            water_count = 0 # 인접한 바다의 개수

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                # 얼음이었는데(visitied_ice = True) 녹아서 바다가 된 경우에는 바다로 생각하면 안됨
                if not visited_ice[nx][ny]:
                    if graph[nx][ny] <= 0:
                        water_count += 1
                    else:
                        linked_ice.append((nx,ny))
            
            # 주변 바다의 개수만큼 얼음 제거
            graph[x][y] -= water_count
            # 제거했을 때 바다가 된다면, ice의 값을 0(바다)로 바꿈
            if graph[x][y] <= 0:
                ice[(x,y)] = 0

year = 0
# 모든 얼음이 바다가 되는 것보다 빙산의 덩어리가 2개로 나뉘는 것이 더 빠르기 때문에 while문의 조건을 모든 얼음이 바다가 될 때까지로 설정
while sum(ice.values()) > 0: 
    dfs_count = 1 # dfs 사이클 수 = 빙산의 덩어리 수
    visited_ice = [[False] * M for _ in range(N)]

    for key,value in ice.items():
        # 아직 다 녹지 않았고, 방문하지 않은 얼음일 경우만
        # 만약 빙산의 덩어리가 1개라면, 첫번째 dfs에서 모든 얼음을 탐색할 것이고, 모든 얼음이 방문처리 되기 때문에 dfs는 한번만 실행됨
        # 빙산의 덩어리가 여러개라면, 방문하지 않은 얼음이 있기 때문에 dfs를 여러번 실행함
        if value and not visited_ice[key[0]][key[1]]:
            if dfs_count == 2:
                print(year)
                exit(0)
            dfs([key[0],key[1]])
            dfs_count += 1

    # for 문을 다 돌아도 dfs가 2번 실행되지 않았다면, 이번 해에는 빙산이 2개로 나뉘지 않았다는 의미
    year += 1

# while 문이 끝날 때까지 (모든 얼음이 바다가 될 때까지) 빙산이 두개로 나뉘지 않는다면 0을 출력
print(0)