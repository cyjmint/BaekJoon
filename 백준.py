##1000번
a, b = input("숫자를 두개 입력하세요 : ").split()
print(a+b) #input().split()은 결과값이 string

a, b = map(int, input("a, b : ").split()) #결과값을 int로 변환
print(a+b)

print(sum(map(int, input("a, b : ").split())))

a = list(range(1,11))
print(a)    

A = []
B = []
for i in list(range(1,10)):
    A.append(i)
    B.append(i)
print(A); print(B)    

#정답
A, B = map(int, input().split())
if A in list(range(1,10)) and B in list(range(1,10)):
    print(A+B)
else:
    pass

#한 줄 정답
print(sum(list(map(int, input().split()))))
