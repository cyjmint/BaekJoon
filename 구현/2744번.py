s = input()
l = []
for i in range(len(s)):
    if s[i].isupper() == True:
        l.append(s[i].lower())
    else:
        l.append(s[i].upper())

print(''.join(l))