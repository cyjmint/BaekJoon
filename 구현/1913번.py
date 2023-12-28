n = int(input())
num = int(input())

dx = [-1,0,1,0]
dy = [0,1,0,-1]  # 상, 우, 하, 좌 순서
graph = [[0]*n for _ in range(n)]

number = 2 #좌표에 넣을 자연수
x = n//2
y = n//2 #시작 위치
graph[x][y] = 1

repeat = 1 #좌표를 같은 방향으로 움직일 횟수
i = 0 # dx,dy 가리키는 변수

answer = [x+1,y+1] #찾고자 하는 자연수의 좌표는 1부터 시작하기 때문에, x축과 y축에 1을 더해야 함
while x != 0 or y != 0: #(0,0)가 될 때까지 반복
    flag = 0
    for _ in range(2): #반복되는 패턴이 2번씩 나타남
        for _ in range(repeat):
            x += dx[i]
            y += dy[i]
            graph[x][y] = number
            if number == num:  # 위치를 찾고자 하는 자연수이면 answer에 위치 저장
                answer = [x+1,y+1] 
            if x == 0 and y == 0: 
                flag = 1
                break
            number += 1 #좌표를 한번 움직였으니 숫자 +1
        if flag == 1: 
            break
        i = (i+1)%4
    repeat += 1

for i in graph:
    print(*i)
   
print(*answer)