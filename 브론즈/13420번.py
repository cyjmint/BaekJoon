T = int(input())
for i in range(T):
    a = input().split()
    if eval(''.join([a[0],a[1],a[2]]))==int(a[-1]):
        print('correct')
    else:
        print('wrong answer')