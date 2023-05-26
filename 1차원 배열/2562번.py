data = []
for i in range(9):
    data.append(int(input()))
m = max(data)
id = data.index(max(data))
print(m), print(id+1)