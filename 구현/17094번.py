import sys
input = sys.stdin.readline

n = int(input())
s = input()
a = 0; b = 0
for i in range(n):
    if s[i] == '2':
        a += 1
    else:
        b += 1

if a > b:
    print(2)
if a < b:
    print('e')
if a == b:
    print('yee')