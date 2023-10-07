n,k = map(int,input().split())
student = {10:0,11:0,20:0,21:0,30:0,31:0,40:0,41:0,50:0,51:0,60:0,61:0}
for i in range(n):
    s,y = map(int,input().split())
    student[y*10+s] += 1

rooms = 0
for v in student.values():
    if v == 0:
        pass
    else:
        for n in range(1,max(student.values())//k+2):
            if v <= k*n:
                rooms += n
                break

print(rooms)