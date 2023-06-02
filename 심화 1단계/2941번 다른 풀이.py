#내 질문에 답변 해주신 분의 코드
#크로아티아 알파벳이 2글자 또는 3글자인데, 이를 하나의 문자로 바꾸면 되는 문제였다.

g=['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
a=input()
for i in g:
    a=a.replace(i,'1')
print(len(a))