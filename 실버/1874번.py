n = int(input())
seq = [int(input()) for _ in range(n)] #입력된 수열 리스트
stack = [] #1~n까지의 수를 넣을 스택
opr = [] #연산자

k = 0; i = 1; a = True
while k < n:
    if a:
        stack.append(i)
        opr.append('+')
    else:
        pass

    if len(stack) == 0:
        i += 1
        a = True
        continue
    
    if stack[-1] == seq[k]:
        stack.pop()
        opr.append('-')
        k += 1
        a = False
    else:
        i += 1
        a = True
    
    if i > n:
        break

if k == n:
    for i,v in enumerate(opr):
        print(v)
else:
    print('NO')