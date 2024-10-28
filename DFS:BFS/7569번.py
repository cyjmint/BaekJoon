import sys
from collections import deque
input = sys.stdin.readline

M,N,H = map(int,input().split())
graph = []
for _ in range(H):
    graph.append([list(map(int,input().split())) for _ in range(N)])

dx = [0,0,0,0,1,-1]
dy = [0,0,1,-1,0,0]
dz = [1,-1,0,0,0,0]

def bfs(graph,q):
    while q:
        x,y,z = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx <= N-1 and 0 <= ny <= M-1 and 0 <= nz <= H-1:
                if graph[z][x][y] != 0 and graph[nz][nx][ny] == 0:
                    graph[nz][nx][ny] = graph[z][x][y] + 1
                    q.append([nx,ny,nz])

q = deque()
for z in range(H):
    for x in range(N):
        for y in range(M):
            if graph[z][x][y] == 1:
                q.append([x,y,z])

bfs(graph,q)

ans = 1
for z in range(H):
    for x in range(N):
        for y in range(M):
            if graph[z][x][y] == 0:
                print(-1)
                exit(0)
            else:
                ans = max(ans, graph[z][x][y])

print(ans-1)