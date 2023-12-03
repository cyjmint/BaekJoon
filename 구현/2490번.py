for _ in range(3):
    n = list(map(int,input().split()))
    if sum(n) == 0:
        print('D')
    if sum(n) == 1:
        print('C')
    if sum(n) == 2:
        print('B')
    if sum(n) == 3:
        print('A')
    if sum(n) == 4:
        print('E')