n = int(input())
for i in range(n):
    s = input()
    stack = []
    for v in s:
        stack.append(v)
        if len(stack) != 1:
            if stack[-2:] == ['(',')']:
                del stack[-2]
                del stack[-1]
            else:
                pass
        else:
            pass
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')