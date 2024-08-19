import sys
input = sys.stdin.readline

num = list(input().strip())
ans = 1

# 1부터 1씩 올리면서 겹치는 부분이 있는지 확인
# 지워진 수가 어떤 자리의 수인지 모르고 지워지지 않은 수가 있을 수 있기 때문에, 겹치는 부분이 있더라도 바로 넘어가지 않고 모두 다 확인해야 함 
while True:
    for a in str(ans):
        if len(num) > 0 and a == num[0]:
            num.pop(0)
    
    if len(num) > 0:
        ans += 1
    else:
        print(ans)
        break