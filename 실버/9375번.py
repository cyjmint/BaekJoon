t = int(input())
for _ in range(t):
    n = int(input())
    ans = 1

    wear = {}
    for _ in range(n):
        name,cloth = input().split()
        if cloth not in list(wear.keys()):
            wear[cloth] = 2 #해당 옷을 입지 않는 경우까지 포함
        else:
            wear[cloth] += 1
    l = list(wear.values())
    
    for i in range(len(l)):
        ans *= l[i]
    
    print(ans-1) #옷을 전부 입지 않는 경우를 제거