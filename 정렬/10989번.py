n = int(input())dic = {}for i in range(1,10001):    dic[i] = 0    for _ in range(n):    num = int(input())    dic[num] += 1    for k,v in dic.items():    if v != 0:        for _ in range(v):            print(k)