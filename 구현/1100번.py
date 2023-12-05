chess = []
for _ in range(8):
    chess.append(list(input()))

ans = 0
for i in range(8):
    for j in range(8):
        if i%2 == 0 and j%2 == 0:
            if chess[i][j] == 'F':
                ans += 1
        if i%2 != 0 and j%2 != 0 :
            if chess[i][j] == 'F':
                ans += 1

print(ans)