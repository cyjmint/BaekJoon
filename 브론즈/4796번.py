n = 1
while True:
    l,p,v = map(int,input().split())
    if l+p+v == 0:
        break
    a = v//p
    b = l*a
    c = v-p*a
    if c <= l:
        print(f"Case {n}: {b+c}")
    else:
        print(f"Case {n}: {b+l}")
    n += 1