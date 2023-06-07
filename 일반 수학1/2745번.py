from string import ascii_uppercase
alp = list(ascii_uppercase)
num = [i for i in range(10,36)]

N = input().split()
n = list(N[0])

for i in range(len(alp)):
    if alp[i] in N[0]:
        for j in range(len(N[0])):
            if N[0][j] == alp[i]:
                n[j] = num[i]
                
n = list(reversed(n))

result = 0
for i in range(len(n)):
    result += int(n[i]) * int(N[1])**i
print(result)