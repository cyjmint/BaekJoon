t = int(input())
for _ in range(t):
    n = int(input())
    rooms = [0]*(n+1)
    for i in range(1,n+1):
        for j in range(1,n//i+1):
            if rooms[i*j] == 0:
                rooms[i*j] = 1
            else:
                rooms[i*j] = 0
    print(sum(rooms))