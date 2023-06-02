#어떻게 같은 알파벳을 중복 처리하지 않게 하지
#dz= 와 z=를 어떻게 구분하지 : 만약 dz=와 z=가 같이 있다면, z=의 개수에서 dz=개수를 빼야함
from string import ascii_lowercase
alp = list(ascii_lowercase)

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
S = input()
l = list(S)
cnt = []
for s in croatia:
    cnt.append(S.count(s))
if 'dz=' in S:
    a = S.count('z=') - S.count('dz=')
    cnt[7] = a
    if a <= 0:
        cnt[7] = 0

n=0
for i in range(len(cnt)):
    if cnt[i] == 1:
        for j in range(len(croatia[i])):
            l.remove(list(croatia[i])[j])
        n += cnt[i]
    else:
        n += cnt[i]

l = [value for value in l if value in alp]

if all(num < 2 for num in cnt):
    n += len(l)
else:
    pass

print(n)

#l이 완성된 이후에 l의 길이를 구해야함
