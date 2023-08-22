dic = {}
for i in range(5):
    dic[sum(list(map(int,input().split())))] = i+1
print(dic[max(dic)],max(dic))