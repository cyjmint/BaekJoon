#시험 성적
A = int(input())
def exam(x):
    if x in list(range(90,101)):
        return print("A")
    elif x in list(range(80,90)):
        return print("B")
    elif x in list(range(70,80)):
        return print("C")
    elif x in list(range(60,70)):
        return print("D")
    elif x not in list(range(0,101)):
        pass
    else:
        return print("F")
    
exam(A)