n = input()
a = n.split('1'); x = n.split('0')
b = ' '.join(a); y = ' '.join(x)
print(min(len(b.split()),len(y.split())))