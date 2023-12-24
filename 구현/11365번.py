while True:
    s = input()
    if s == 'END':
        break
    s = list(reversed(s))
    print(''.join(s))