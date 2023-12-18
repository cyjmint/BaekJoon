q = int(input())
for _ in range(q):
    a = int(input())
    b = list(map(int,bin(a)[2:])) 
    if sum(b) == 1: #2의 거듭제곱이 됨 = 이진수로 나타냈을 때 첫째 자리 수만 1이 됨
        print(1)
    else:
        print(0)

#--------------------------------------#
q = int(input())
for _ in range(q):
    a = int(input())
    while True:
        if a == 1:
            print(1)
            break
        if a % 2 != 0:
            print(0)
            break
        if a % 2 == 0:
            a //= 2

#--------------------------------------#
#보수를 이용하여 계산
q = int(input())
for _ in range(q):
    a = int(input())
    if a&(-a) == a:
        print(1)
    else:
        print(0)

#a가 4라고 하면, 4의 이진수는 100(2), -4의 이진수는 4에 대한 2의 보수인 100(2)이다. 4와 -4를 비트연산 &로 비교하면 100(2)이 되므로, 4&(-4) == 4 가 된다.
#즉 a가 2의 거듭제곱으로 표현될 수 있다면, a&(-a) == a가 성립한다.