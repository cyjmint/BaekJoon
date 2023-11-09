board = input().split('.')

for i in range(len(board)):
    l = len(board[i])
    if l % 4 == 0:
        board[i] = 'A'*l
    if (l % 4) % 2 == 0:
        board[i] = 'A'*4*(l//4) + 'B'*2*((l%4)//2)
    if (l % 4) % 2 != 0:
        board = -1
        break

if board == -1:
    print(board)
else:
    print('.'.join(board))