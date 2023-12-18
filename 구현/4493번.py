T = int(input())
for _ in range(T):
    a,b = 0,0
    n = int(input())
    for _ in range(n):
        p1,p2 = input().split()
        if p1 == 'R':
            if p2 == 'S':
                a += 1
            if p2 == 'P':
                b += 1

        if p1 == 'S':
            if p2 == 'R':
                b += 1
            if p2 == 'P':
                a += 1

        if p1 == 'P':
            if p2 == 'R':
                a += 1
            if p2 == 'S':
                b += 1
        
    if a>b:
        print('Player 1')
    if b>a:
        print('Player 2')
    if a==b:
        print('TIE')
#player 1과 player 2의 이긴 횟수만 비교, 비긴 횟수는 카운트 할 필요 없음