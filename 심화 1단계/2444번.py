N = int(input())
for i in range(2*N-1):
    if i <= N-1:
        S = '*'*(2*(i+1)-1)
        a = (N-1)-i
        print(' ' * a, end = '')
        print(S)
    else:
        X = '*'*((2*N-1)-2*(i-(N-1)))
        b = i-(N-1)
        print(' ' * b, end = '')
        print(X)