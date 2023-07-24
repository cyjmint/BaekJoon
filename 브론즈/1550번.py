N = list(reversed(list(input()))); n = 0
for i in range(len(N)):
    if N[i] == 'A':
        n += 10*16**i
    elif N[i] == 'B':
        n += 11*16**i
    elif N[i] == 'C':
        n += 12*16**i
    elif N[i] == 'D':
        n += 13*16**i
    elif N[i] == 'E':
        n += 14*16**i
    elif N[i] == 'F':
        n += 15*16**i
    else:
        n += int(N[i])*16**i
print(n)

##파이썬에서 2진수, 8진수, 16진수 표현
#접두어 붙이기
42 == 0b101010 #2진수 : 0b
42 == 0o52 #8진수 : 0o
42 == 0x2a #16진수 : 0x
#함수 사용
bin(42) #2진수 
oct(42) #8진수
hex(42) #16진수
#format 사용
format(42,'b')
format(42,'o')
format(42,'x')
#2진수, 8진수, 16진수 -> 10진수
int('101010',2)
int('52',8)
int('2a',16)
