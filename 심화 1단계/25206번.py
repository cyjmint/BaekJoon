a = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
b = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]

data = []
for i in range(20):
    data.append(input().split())

data[:] = (value for value in data if value[2] != 'P')

for j in range(len(data)):
    for i in range(9):
        if data[j][2] == a[i]:
            data[j][2] = b[i]
       
score = []
c = []         
for i in range(len(data)):
    score.append(float(data[i][1])*float(data[i][2]))
    c.append(float(data[i][1]))
n = sum(score) / sum(c)  

print(n)