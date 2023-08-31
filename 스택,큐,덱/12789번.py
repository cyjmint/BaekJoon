n = int(input())
order = list(map(int,input().split()))
l = []

num = 1
while num <= n:
    if len(order) == 0:
        if l[-1] == num:
            l.remove(l[-1])
            num += 1
        else:
            break
    else:
        if len(l) == 0:
            if order[0] == num:
                order.remove(order[0])
                num += 1
            else:
                l.append(order[0])
                order.remove(order[0])
        else:
            if order[0] == num:
                order.remove(order[0])
                num += 1
            elif l[-1] == num:
                l.remove(l[-1])
                num += 1
            else:
                l.append(order[0])
                order.remove(order[0])

if len(l) == 0:
    print('Nice')
else:
    print('Sad')