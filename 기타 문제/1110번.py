N = int(input())
n = N
num = 0
while True:
    x = n//10 + n%10
    n1 = int(f'{n%10}' + f'{x%10}')
    if n1 != N:
        n = n1
        num += 1
    else:
        num += 1
        break
print(num)