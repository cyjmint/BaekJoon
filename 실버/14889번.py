from itertools import combinations,permutations

n = int(input())
score = [list(map(int,input().split())) for _ in range(n)]
members = list(combinations(range(n),n//2))

team_start = [members[i] for i in range(len(members)//2)]
team_link = [members[i] for i in range(len(members)//2, len(members))]
team_link = list(reversed(team_link))

minsub = 1e9
for i in range(len(team_start)):
    score_t1 = 0; score_t2 = 0
    team1 = list(permutations(team_start[i],2))
    team2 = list(permutations(team_link[i],2))
    for j in range(len(team1)):
        a = team1[j][0]; b = team1[j][1]
        x = team2[j][0]; y = team2[j][1]
        score_t1 += score[a][b]
        score_t2 += score[x][y]
    minsub = min(minsub, abs(score_t1-score_t2))

print(minsub)