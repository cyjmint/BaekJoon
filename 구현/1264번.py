while True:
    sentence = input()
    dic = {'a':0,'e':0,'i':0,'o':0,'u':0,
           'A':0,'E':0,'I':0,'O':0,'U':0}
    if sentence == '#':
        break
    for k in dic.keys():
        for i in range(len(sentence)):
            if sentence[i] == k:
                dic[k] += 1
    print(sum(dic.values()))