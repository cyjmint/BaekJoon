a0 = [10,10,10,10]
a1 = [1,1,1,1]
a2 = [2,4,8,6]
a3 = [3,9,7,1]
a4 = [4,6,4,6]
a5 = [5,5,5,5]
a6 = [6,6,6,6]
a7 = [7,9,3,1]
a8 = [8,4,2,6]
a9 = [9,1,9,1]

T = int(input())
for i in range(T):
    a,b = list(map(int,input().split()))
    a = a%10
    b = b%4-1
    if a == 0:
        print(a0[b])
    elif a == 1:
        print(a1[b])
    elif a == 2:
        print(a2[b])
    elif a == 3:
        print(a3[b])
    elif a == 4:
        print(a4[b])
    elif a == 5:
        print(a5[b])
    elif a == 6:
        print(a6[b])
    elif a == 7:
        print(a7[b])
    elif a == 8:
        print(a8[b])
    else:
        print(a9[b])
