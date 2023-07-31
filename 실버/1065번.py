N = int(input())
if N < 100:
    ans = N
else:
    ans = 99
    for v in range(100,N+1):
        s = str(v)
        d = int(s[0])-int(s[1])
        if (int(s[0]) + d == int(s[1]) and int(s[1]) + d == int(s[2])) or (int(s[0]) - d == int(s[1]) and int(s[1]) - d == int(s[2])):
            ans+=1
            

print(ans)