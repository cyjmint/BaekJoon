data = []
l = []
for i in range(5):
    data.append(input().strip())
    l.append(len(data[i]))
    
s = []
for j in range(max(l)):
    for t in data:
        try :
            s.append(t[j])
        except IndexError :
            pass
           
for i in range(len(s)):
    for j in range(len(s[i])):
        print(s[i][j], end = '')


