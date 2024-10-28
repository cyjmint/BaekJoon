import sys
input = sys.stdin.readline

# N : 가로, M : 세로, L : 한 변의 길이, K : 별똥별 개수
N,M,L,K = map(int,input().split())
star = [list(map(int,input().split())) for _ in range(K)]

# 두 좌표의 x값과 y값 중에서 최소값을 사용해서 두 좌표를 가장자리에 포함시키는 사각형의 꼭짓점 좌표를 생성
# 해당 사각형 안에 몇 개의 좌표가 포함되는지 확인
# 굳이 최소값 조건을 걸지 않아도 문제 풀이에 지장은 없음
ans = K
for x,_ in star:
    for _,y in star:
        tmp = K
        for a,b in star:
            if x <= a <= x+L and y <= b <= y+L:
                tmp -= 1
        ans = min(ans,tmp)

print(ans)