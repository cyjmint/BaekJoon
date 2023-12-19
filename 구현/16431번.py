br,bc = map(int,input().split())
dr,dc = map(int,input().split())
jr,jc = map(int,input().split())

b = max(abs(br-jr),abs(bc-jc)) 
#bessie는 상하좌우 대각선 모두 이동할 수 있기 때문에, 대각선으로 충분히 이동한 다음 남은 칸만큼 상하좌우로 이동하면 됨
#즉, x축과 y축 중에 가장 멀리 떨어진 좌표의 차이가 움직이는데 걸리는 초
d = abs(dr-jr)+abs(dc-jc)
#daisy는 상하좌우로만 이동할 수 있기 때문에, x축과 y축 좌표 각각의 차이의 합이 움직이는데 걸리는 초
if b < d:
    print('bessie')
if d < b:
    print('daisy')
if d == b:
    print('tie')