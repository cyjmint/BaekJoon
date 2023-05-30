from string import ascii_uppercase
alp = list(ascii_uppercase)
T = [3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10]
S = input()
N = []
for i in range(len(list(S))):
    N.append(T[alp.index(S[i])])
print(sum(N))
