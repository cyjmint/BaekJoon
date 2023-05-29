from string import ascii_lowercase
alp = list(ascii_lowercase)
S = input()

for i in range(len(alp)):
    if alp[i] in list(S):
        print(S.index(alp[i]), end = ' ')
    else:
        print(-1, end = ' ')
        