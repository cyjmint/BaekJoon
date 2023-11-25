n = int(input())
time = [list(map(int,input().split())) for _ in range(n)]
time = sorted(time, key = lambda x : x[0])
time = sorted(time, key = lambda x : x[1])

ans = 1; j = 0
for i in range(1,n):
    if time[j][1] <= time[i][0]:
        ans += 1
        j = i

print(ans)

#회의 시간이 최소인 회의부터 선택하는 것이 최적의 경우
#최소가 아닌 회의부터 선택하면, 최소일 때보다 회의 후 남은 회의 시간이 적기 때문에, 같은 수의 회의가 주어졌을 때 첫 회의 시간이 최소인 경우보다 남은 회의들을 최대로 배치 할 수가 없음
#즉, 시작 시간이 같은 경우에는 끝 시간이 더 빠른 회의를 먼저 고려해야 함.

#끝 시간이 같은 경우에는 시작 시간이 더 빠른 회의를 먼저 고려해야 함.
#두개의 회의 (2,3),(3,3)가 있다고 하자. 두 회의의 끝 시간은 3으로 같다. 이때 시작 시간이 더 늦은 회의부터 선택한다면 (2,3) 회의는 선택할 수 없게 된다. 하지만 (2,3) 회의를 먼저 선택하면 (3,3) 회의까지 선택할 수 있다.

#그러므로 회의 시간이 주어졌을 때, 끝 시간이 오름차순 정렬된 상태에서 시작 시간을 오름차순 정렬해야 한다.
#코드로 구현할 때는, 시작 시간을 먼저 정렬한 후에 끝 시간을 정렬하면 됨.
#파이썬은 정렬 안정성을 보장하기 때문에, 끝 시간을 정렬할 때 시작 시간을 정렬했을 때의 순서가 보장됨.