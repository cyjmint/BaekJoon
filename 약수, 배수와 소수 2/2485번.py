N = int(input())
n = [int(input())for i in range(N)]
num = [n[i+1]-n[i] for i in range(N-1)]

for i in range(len(num)-1):
    x,y = max(num[i],num[i+1]),min(num[i],num[i+1]);r=x%y
    while r:x,y=y,r;r=x%y
    num[i+1]=y

print(((max(n)-min(n)-1)//y)-(len(n)-2))