N = list(reversed(list(input()))); n = 0
for i in range(len(N)):
    if N[i] == 'A':
        n += 10*16**i
    elif N[i] == 'B':
        n += 11*16**i
    elif N[i] == 'C':
        n += 12*16**i
    elif N[i] == 'D':
        n += 13*16**i
    elif N[i] == 'E':
        n += 14*16**i
    elif N[i] == 'F':
        n += 15*16**i
    else:
        n += int(N[i])*16**i
print(n)