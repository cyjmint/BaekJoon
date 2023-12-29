n = int(input())
cow = [] #소의 번호과 위치 정보 리스트
for _ in range(n):
    cow.append(list(map(int,input().split())))

ans = 0 #길을 건넌 횟수
for i in range(n): #i번째 관찰
    for j in range(i+1,n): #i번째 관찰 이후인 j번째 관찰
        if cow[i][0] == cow[j][0]: #만약 i번째 관찰한 소의 번호와 j번째 관찰한 소의 번호가 같고
            if cow[i][1] != cow[j][1]: #위치 정보는 다르다면
                ans += 1 #소가 길을 건넜다는 의미
            break #소가 길을 건넜는지 안 건넜는지 알게 됐기 때문에, i번째 관찰한 소의 정보는 더 이상 필요가 없음. 다음 관찰로 넘어감.

print(ans)