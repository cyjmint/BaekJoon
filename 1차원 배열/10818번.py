#첫번째 풀이
#N = int(input())
#data = list(map(int,input().split()))
#x = [data[0], data[1]]
#for i in range(N):
#    if data[i] >= x[0]:
#        x[0] = data[i]
#    if data[i] <= x[1]:
#        x[1] = data[i]
#print(x[1], end = ' ')
#print(x[0])
#백준 채점 결과로 IndexError가 나오는데, N = 1일 때 list index out of range이기 때문이다.

#두번째 풀이
N = int(input())
data = list(map(int,input().split()))
x = [data[0], data[0]]
for i in range(N):
    if data[i] >= x[0]:
        x[0] = data[i]
    if data[i] <= x[1]:
        x[1] = data[i]
print(x[1], end = ' ')
print(x[0])
#정답!