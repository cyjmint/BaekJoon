N, M = list(map(int,input().split()))
data = []
for i in range(N):
    data.append(list(input()))

a = list('WBWBWBWB')
b = list('BWBWBWBW')

num = []
for x in range(M-7): #x축
    for y in range(N-7): #y축
        n = 0; m = 0 #n:첫번째 줄이 a와 같은 경우, m:첫번째 줄이 b와 같은 경우
        for j in range(y,y+8): #data를 8x8로 나눌 sample의 y축
            s = [data[j][v] for v in range(x,x+8)] #v:sample의 x축, s:sample의 (j+1)번째 줄
            for z in range(8): #홀수번째 줄이 a와 같다면, 짝수번째 줄은 b와 같아야 함, 그 반대도 성립
                if j%2 == 0:
                    if s[z] != a[z]:
                        n += 1
                    if s[z] != b[z]:
                        m += 1
                else:
                    if s[z] != a[z]:
                        m += 1
                    if s[z] != b[z]:
                        n += 1
        num.append(min(m,n))
            
print(min(num))



