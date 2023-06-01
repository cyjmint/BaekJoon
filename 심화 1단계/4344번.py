#import sys
#input = sys.stdin.readline

C = int(input())
data = []
for i in range(C):
    s = 0
    m = 0
    p = 0
    data.append(list(map(int, input().split())))
    s = sum(data[i]) - data[i][0]
    m = s/data[i][0]
    o = []
    for j in range(1,len(data[i])):
        if data[i][j] > m:
            o.append(data[i][j])
    p = (len(o)/(len(data[i])-1))*100
    print('%0.3f%s'%(p,'%'))


