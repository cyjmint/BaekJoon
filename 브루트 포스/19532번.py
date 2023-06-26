a,b,c,d,e,f = list(map(int,input().split()))
x = (c*e-b*f)/(a*e-b*d)
y = (c*d-f*a)/(b*d-a*e)
print(int(x), end = ' '); print(int(y))
