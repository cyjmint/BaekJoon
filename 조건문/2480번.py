a, b, c = list(map(int, input().split()))

def dice(x,y,z):
    if x==y==z:
        result = 10000 + x*1000
    elif x != y and y != z and x != z:
        result = max([x,y,z]) * 100
    else:
        count = {}
        l = [x,y,z]
        for i in l:
            try: count[i] += 1
            except: count[i] = 1
        for key, value in count.items():
            if value >= 2:
                result = 1000 + key*100
    return print(result)

dice(a,b,c)