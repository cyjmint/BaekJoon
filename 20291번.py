n = int(input())
dic = {}
for i in range(n):
    file = list(input().split('.'))
    if file[1] in dic.keys():
        dic[file[1]] += 1
    else:
        dic[file[1]] = 1

for k,v in sorted(dic.items()):
    print(k,v)