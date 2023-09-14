l = [int(v) for v in list(input())]
l = sorted(l,reverse=True)
l = list(map(str,l))
print(''.join(l))