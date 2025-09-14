import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    move = [+2,+1,+2,-1,-2,+1,-2,-1,+1,+2,+1,-2,-1,+2,-1,-2]
    
    target_x, target_y = togo
    visited = [[0]*size for _ in range(size)]
    queue = deque([])
    queue.append(current)
    
    while queue:
        x,y = queue.popleft()

        if x == target_x and y == target_y:
            print(visited[x][y])
            return
        
        for a in range(0,15,2):
            x_1 = x + move[a]; y_1 = y + move[a+1]
            if 0 <= x_1 <= size-1 and 0 <= y_1 <= size-1 and visited[x_1][y_1] == 0:
                visited[x_1][y_1] = visited[x][y] + 1
                queue.append((x_1,y_1))

T = int(input())
for _ in range(T):
    size = int(input())
    current = list(map(int,input().split()))
    togo = list(map(int,input().split()))
    bfs()