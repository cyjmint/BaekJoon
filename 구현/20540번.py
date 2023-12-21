mbti = input()
mbti2 = []

if mbti[0] == 'I':
    mbti2.append('E')
else:
    mbti2.append('I')

if mbti[1] == 'S':
    mbti2.append('N')
else:
    mbti2.append('S')

if mbti[2] == 'T':
    mbti2.append('F')
else:
    mbti2.append('T')

if mbti[3] == 'J':
    mbti2.append('P')
else:
    mbti2.append('J')

print(''.join(mbti2))