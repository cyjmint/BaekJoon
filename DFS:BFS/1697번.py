from collections import deque
import sys
input = sys.stdin.readline

N,K = map(int,input().split())

# 0 <= N,K <= 100,000
visited = [0] * 100001

def bfs(start, target, visited):
    q = deque()
    visited[start] = 1 # 시작을 1로 초기화했기 때문에 결과값에 1을 빼야함
    q.append(start)

    while q:
        subin = q.popleft()
        # 수빈이의 이동 경우의 수
        subin_move = [subin-1, subin+1, subin*2]
        for i in range(3):
            move = subin_move[i]
            # 수빈이가 이동한 위치가 이전에 방문한 곳이 아니라면 1초 더하기
            if 0 <= move <= 100000 and visited[move] == 0:
                visited[move] = visited[subin] + 1
                q.append(move)
            
            # 만약 수빈이가 이동한 위치가 동생 위치라면 1초 더하고 총 소요 시간 출력
            if move == target:
                return visited[subin] + 1

# 위치가 처음부터 같으면 움직일 필요가 없음
if N == K:
    print(0)
else:
    print(bfs(N,K,visited)-1)