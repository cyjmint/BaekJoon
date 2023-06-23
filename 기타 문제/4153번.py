while True:
    a,b,c = map(int,input().split())
    if a==0 and b==0 and c==0:
        break
    if max(a,b,c)**2 == min(a,b,c)**2 + ((a+b+c)-max(a,b,c)-min(a,b,c))**2:
        print('right')
    else:
        print('wrong')