a1, a0 = list(map(int,input().split()))
c = int(input())
n0 = int(input())

if c < a1:
    print(0)
elif a0 > 0 and (a1*n0+a0) > c*n0:
    print(0)
else:
    print(1)
    
#그래프를 사용해서 시각적으로 표현하고, 
#참이 되는 조건들의 공통점을 묶으면 됨