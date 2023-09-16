n = int(input())
num = list(map(int,input().split()))
s_num = sorted(set(num))

dic = {}
for i in range(len(s_num)):
    dic[s_num[i]] = i
    
for i in range(n):
    num[i] = dic[num[i]]

print(*num)