#그래프 -> 인접 리스트 또는 인접 행렬
#양방향 그래프 -> 간선을 두번 저장

n,m,v = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = []

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

#DFS
def dfs(x):
    visited.append(x)
    for i in sorted(graph[x]):
        if i not in visited:
            dfs(i)

#BFS
queue = []
order = 0
queue.append(v)
while order < len(queue):
    x = queue[order]
    for i in sorted(graph[x]):
        if i not in queue:
            queue.append(i)
    order += 1

dfs(v)
print(*visited)
print(*queue)