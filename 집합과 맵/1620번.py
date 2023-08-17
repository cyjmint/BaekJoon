n,m = map(int,input().split())
dic = {}

for i in range(1,n+1):
    dic[str(i)] = input()
re_dic = {v:k for k,v in dic.items()}

for i in range(m):
    q = input()
    try:
        print(dic[q])
    except:
        print(re_dic[q])