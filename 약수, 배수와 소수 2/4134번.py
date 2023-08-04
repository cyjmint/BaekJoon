for i in range(int(input())):
    n = int(input())
    if n == 0:
        n += 1
    x = n
    while x:
        if x == 1:
            x+=1
        elif all(x%y!=0 for y in range(2,int(x**(1/2))+1)):
            print(x)
            break
        else:
            x+=1