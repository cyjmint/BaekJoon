#윤년
year = int(input())
print('1' if year%4 == 0 and (year%100 != 0 or year%400 == 0) else '0')


#범위를 설정한다면
def leap(x):
    if x not in list(range(1,4001)):
        pass
    else:
        return print('1' if year%4 == 0 and (year%100 != 0 or year%400 == 0) else '0')

leap(year)