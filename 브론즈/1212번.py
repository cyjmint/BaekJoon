n = input()
N = 0
l = []
for num in n:
    num = int(num)
    if num == 0:
        l.append('000')
    elif num == 1:
        l.append('001')
    elif num == 2:
        l.append('010')
    elif num == 3:
        l.append('011')
    elif num == 4:
        l.append('100')
    elif num == 5:
        l.append('101')
    elif num == 6:
        l.append('110')
    else:
        l.append('111')
        
l[0] = str(int(l[0]))
print(''.join(l))