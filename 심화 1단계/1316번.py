#해당 알파벳의 인덱스가 연속하지 않으면 그룹 단어가 아님

from string import ascii_lowercase
alp = list(ascii_lowercase)

def func(x): #연속하는 인덱스는 1씩 차이난다.
    if len(x) == 1:
        return True
    else:
        return all(x[i] - x[i-1] == 1 for i in range(1,len(x)))
    
N = int(input())
n = 0
for i in range(N):
    ind = []
    w = input()
    for j in range(len(alp)):
        if alp[j] in w:
            i = list(filter(lambda x: w[x] == alp[j], range(len(w)))) 
                #filter함수와 lambda 함수를 사용해서 x 출력, x는 해당 알파벳이 w의 어느 인덱스에 있는가
            ind.append(i)
    if all(func(ind[k]) == True for k in range(len(ind))):
        n += 1
        
print(n)