n = int(input())
num = list(map(int,input().split()))

score = []
if num[0] == 0:
    score.append(0)
else:
    score.append(1)

for i in range(1,n):
    if num[i] == 1 and score[i-1] != 0:
        score.append(score[i-1]+1)
    if num[i] == 1 and score[i-1] == 0:
        score.append(1)
    if num[i] == 0:
        score.append(0)

print(sum(score))