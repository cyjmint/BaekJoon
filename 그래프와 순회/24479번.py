import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

order = 1
def dfs(r):
    global order
    visited[r] = order
    for x in sorted(graph[r]):
        if visited[x] == 0:
            order += 1
            dfs(x)

n,m,r = map(int,input().split())
graph = [[] for _ in range(n+1)] #인접 리스트
visited = [0] * (n+1)

for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v) #양방향 리스트이기 때문에 간선 u에 한번 저장하고 간선 v에 한번 더 저장한다.
    graph[v].append(u)
    
dfs(r)
for i in range(1,n+1):
    print(visited[i])