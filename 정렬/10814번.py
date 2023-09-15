n = int(input())
people = []
for i in range(n):
    people.append(input().split())
    people[i][0] = int(people[i][0])
    
s_people = sorted(people, key = lambda x: [x[0]])

for v in s_people:
    print(*v)