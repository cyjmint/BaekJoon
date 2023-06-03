data = []
for i in range(9):
    data.append(list(map(int, input().split())))

maxvalue = max(map(max,data))
print(maxvalue)

for i in range(9):
    for j in range(9):
        if data[i][j] == maxvalue:
            print(i+1, end = ' ')
            print(j+1)
            