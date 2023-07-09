N = int(input())
s = list(reversed(list(input())))

for n in range(N):
    if s[n] == 'A':
        s[n] = 0
    elif s[n] == 'G':
        s[n] = 1
    elif s[n] == 'C':
        s[n] = 2
    else:
        s[n] = 3

k = 0
while k < N-1:
    n=k+1
    if s[k] == 0 and s[n] == 1:
        s[n] = 2
        k+=1
    elif (s[k] == 0 and s[n] == 2) or (s[k] == 1 and s[n] == 3):
        s[n] = 0
        k+=1
    elif (s[k] == 0 and s[n] == 3) or (s[k] == 2 and s[n] == 3):
        s[n] = 1
        k+=1
    elif s[k] == 1 and s[n] == 2:
        s[n] = 3
        k+=1
    elif s[k] > s[n]:
        s[k], s[n] = s[n], s[k]
        continue
    else:
        k+=1

if s[N-1] == 0:
    print('A')
elif s[N-1] == 1:
    print('G')
elif s[N-1] == 2:
    print('C')
else:
    print('T')