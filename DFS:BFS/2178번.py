import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int,input().rstrip())) for _ in range(n)] #파이썬에서 문자열은 배열처럼 작동함

#최소 거리를 구하는 문제 = BFS -> 큐를 사용해서 해결

dx = [-1,1,0,0] #상하로 움직이도록 함
dy = [0,0,-1,1] #좌우로 움직이도록 함
#대각선으로 움직이지 않기 때문에 상하로 움직일 떄는 좌우를 고정시켜야 하고, 좌우로 움직일 때는 상하를 고정시켜야 함

def bfs(x,y):
    queue = deque() #큐 생성, FIFO
    queue.append((x,y)) #제일 먼저 탐색을 시작하는 위치인 (0,0)을 append

    while queue: 
        #만약 목적지에 도착하면, 목적지의 위치를 pop할 것이고, pop한 위치는 목적지이기 때문에 상하좌우 그 어디에도 값이 1인 위치는 없다(목적지에 가는 동안 이동할 때마다 칸의 값이 +1 되기 때문). 그러므로 queue에 새로운 원소를 append할 수 없다.
        #즉, queue에 원소가 없다면 목적지에 도착했다는 의미다.
        x,y = queue.popleft() #탐색을 시작할 위치 pop

        for i in range(4):
            nx = x+dx[i] #좌표를 상하로 움직이게 함
            ny = y+dy[i] #좌표를 좌우로 움직이게 함

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                #상하좌우로 움직인 위치의 값이 1이라면(움직인 후의 칸이 이동할 수 있는 칸이라면)
                queue.append((nx,ny)) #해당 위치를 append한다(해당 칸으로 이동한다)
                graph[nx][ny] = graph[x][y] + 1 #해당 위치로 이동하기 위해 한번 움직였으므로 +1

    return graph[n-1][m-1]

print(bfs(0,0))