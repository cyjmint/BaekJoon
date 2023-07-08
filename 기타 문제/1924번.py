x,y = list(map(int,input().split()))
day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

n = 0
for i in range(1,x):
    if i == 2:
        n += 28
    elif i == 4 or i == 6 or i == 9 or i == 11:
        n += 30
    else:
        n += 31

result = (n+y)%7
print(day[result])