n = int(input())
num = list(int(input()) for i in range(n))
if sum(num) > n/2:
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')