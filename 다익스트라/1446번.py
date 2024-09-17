import sys, heapq
input = sys.stdin.readline

n,d = map(int,input().split())

graph = [[] for _ in range(d+1)]
dist = [1e9] * (d+1)

# d까지의 각 거리를 노드로 생각
# i : 시작 노드 / (도착 노드, 거리)
for i in range(d):
    graph[i].append((i+1, 1))

# start에서 end까지의 거리를 추가
for _ in range(n):
    start, end, length = map(int,input().split())
    if end <= d:
        graph[start].append((end, length))

# 우선순위 큐를 사용해서 다익스크라 알고리즘을 구현할 때는, 방문 테이블을 정의할 필요 없음
# 우선순위 큐를 사용하면 자동으로 가장 최단 거리 노드를 가장 앞으로 정렬해주기 때문에 기존에 기록한 최단 거리보다 길다면 무시하면 됨
# 더 짧은 노드가 나오면 우선순위 큐에 넣어주면 됨
q = []
heapq.heappush(q, (0,0)) # q에 (거리, 노드)를 추가
dist[0] = 0 # 시작 노드에서 시작 노드로 갈 때 거리는 0

while q:
    _, node = heapq.heappop(q) 

    # 인접 노드들 확인
    for near_node, weight in graph[node]:
        cost = dist[node] + weight # 노드까지 가는 거리 + 노드에서 인접 노드까지의 거리
        if dist[near_node] > cost: # 기존 거리보다 가까워지면 업데이트
            dist[near_node] = cost
            heapq.heappush(q, (cost, near_node)) # 업데이트 될 때만 우선 순위 큐에 추가

print(dist[d])