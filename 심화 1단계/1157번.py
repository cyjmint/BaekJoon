S = input()
S = list(S.upper())
S2 = list(set(S)) 

cnt = []
for i in range(len(S2)):
    cnt.append(S.count(S2[i]))
if cnt.count(max(cnt)) >= 2:
    print('?')
else:
    print(S2[cnt.index(max(cnt))])