import sys
input = sys.stdin.readline

def init(start):
    for i in range(start, start+N):
        tree[i] = num[i-start+1]

    for i in range(start-1,0,-1):
        tree[i] = tree[i * 2] + tree[i * 2 + 1]

def update(start, what, value):
    change_index = start + what - 1
    tree[change_index] = value

    while change_index != 1:
        change_index //= 2
        tree[change_index] = tree[change_index * 2] + tree[change_index * 2 + 1]

def interval_sum(start, left, right, sum):
    sum_left = left + start - 1
    sum_right = right + start
    
    while sum_left < sum_right:
        if sum_left % 2 != 0:
            sum += tree[sum_left]
            sum_left += 1

        if sum_right % 2 != 0:
            sum_right -= 1
            sum += tree[sum_right]
        
        sum_right //= 2
        sum_left //= 2

    return sum

N,M,K = map(int,input().split())
num = [0] + [int(input().rstrip()) for _ in range(N)]
index = 1048576
total = index * 2
tree = [0] * total
init(index)

for _ in range(M+K):
    a,b,c = map(int,input().split())
    if a == 1:
        update(index, b, c)
    if a == 2:
        print(interval_sum(index, b, c, 0))