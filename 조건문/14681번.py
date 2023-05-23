#사분면 고르기
a = int(input())
b = int(input())

def Qua(x,y):
    if x not in range(-1000,1001) or y not in range(-1000,1001) or x == 0 or y == 0:
        pass
    else:
        return print('1' if x > 0 and y > 0 else 
                     '2' if x < 0 and y > 0 else 
                     '3' if x < 0 and y < 0 else '4')
    
Qua(a,b)

