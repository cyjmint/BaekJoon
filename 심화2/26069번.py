n = int(input())
meets = []
for i in range(n):
    a,b = input().split()
    meets.append([a,b])
    
dance = {'ChongChong'}
for meet in meets:
    a,b = meet
    if a in dance or b in dance:
        dance.add(a)
        dance.add(b)

print(len(dance))