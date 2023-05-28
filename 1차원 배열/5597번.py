#import sys
#input = sys.stdin.readline

data1 = []
for i in range(28):
    data1.append(int(input()))
data2 = []
for j in range(30):
    data2.append(j+1)
s1 = set(data1)
s2 = set(data2)
data3 = list(s2 - s1)
print(min(data3))
print(max(data3))
