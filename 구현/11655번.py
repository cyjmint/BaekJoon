from string import ascii_lowercase, ascii_uppercase
alp_l = list(ascii_lowercase)
alp_u = list(ascii_uppercase)

s = list(input())

for i in range(len(s)):
    if s[i] in alp_l:
        j = alp_l.index(s[i])
        if j+13 < len(alp_l):
            s[i] = alp_l[j+13]
        else:
            z = j+13-len(alp_l)
            s[i] = alp_l[z]
    if s[i] in alp_u:
        j = alp_u.index(s[i])
        if j+13 < len(alp_u):
            s[i] = alp_u[j+13]
        else:
            z = j+13-len(alp_u)
            s[i] = alp_u[z]

print(''.join(s))