n=int(input())
i=0
while n:
    i+=1
    n-='666'in'%s'%i #'666'in'%s'%i의 결과가 True라면, n-=1이 됨. 
                     #n = 0(False)가 될 때까지 while문 반복
                     #즉, 666이 포함된 n번째 수가 나올 때까지 i에 1을 더하고, n번째 수에서 반복문이 종료됨.
print(i)