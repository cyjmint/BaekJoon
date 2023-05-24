#45분 일찍 알람 설정하기
H, M= list(map(int,input().split()))

def alarm(x,y):
    if x not in range(0,24) or y not in range(0,60):
        pass
    else:
        h = ((x*60+y)-45) // 60
        m = ((x*60+y)-45) % 60
    if h < 0:
        h += 24
    return print(h, end = ' '), print(m)

alarm(H,M)
