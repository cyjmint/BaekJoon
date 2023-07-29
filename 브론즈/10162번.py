t = int(input())
A,B,C = 300,60,10

a = t//A
b = (t%A)//B
c = ((t%A)%B)//C
n = [a,b,c]

if ((t%A)%B)%C != 0:
    print(-1)
else:
    for i in range(len(n)):
        print(n[i], end = ' ')