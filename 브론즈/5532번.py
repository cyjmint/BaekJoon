l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

i = 1
while c*i < a or d*i < b:
    i += 1

print(l-i)