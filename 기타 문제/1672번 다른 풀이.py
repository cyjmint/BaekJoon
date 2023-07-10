x="AGCT".index
#list.index(x)는 리스트 내 x의 인덱스 값을 출력한다
#x를 "AGCT".index라고 할당했기 때문에, "AGCT".index('A') == x('A')이다.

n=int(input())-1;s=input()
r=s[-1] #s의 가장 마지막 요소를 출력해서 r에 할당

while n:n-=1;r="ACAGCGTAATCGGAGT"[x(s[n])*4+x(r)]
#n이 0이면 false로 인식해서 while문 중단
#"ACAGCGTAATCGGAGT"는 염기서열을 나타낸 2차원 행렬을 한 줄로 표현한 것
#x(s[n]) : s[n]에 해당하는 문자가 몇번째 행 또는 열에 있는가
#x(s[n])*4 : 해당 행 또는 열의 첫번째 값의 인덱스
#x(r) : s[n+1]에 해당하는 문자가 몇번째 열 또는 행에 있는가
#x(s[n])*4+x(r) : (s[n], s[n+1])에 해당하는 값의 인덱스

print(r)


