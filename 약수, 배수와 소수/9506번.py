while True:
    n = int(input())
    if n == -1:
        break
    F = []
    for i in range(1,n+1):
        if n%i == 0:
            F.append(i)
    if n == sum(F)-n:
        print('%d = %d'%(n,F[0]), end = ' ')
        for i in range(1,len(F)-1):
            print('+',F[i], sep = ' ', end = ' ')
        print()
    else:
        print('%d is NOT perfect.'%(n))        
