while True:
    s = input()
    if s == '.':
        break
    stack = []
    for v in s:
        if v == '(' or v == ')' or v == '[' or v == ']' or v == '.':
            stack.append(v)
        if len(stack) != 1:
            if stack[-2:] == ['(',')'] or stack[-2:] == ['[',']']:
                del stack[-2]
                del stack[-1]
            else:
                pass
        else:
            pass
    if len(stack) == 1:
        print('yes')
    else:
        print('no')