N = int(input())
n = [int(input()) for i in range(N)]

def Merge_Sort(L):
    def sort(s,e):
        if e-s <= 1:
            return
        else:
            m = (e+s)//2
            sort(s,m) #왼쪽 리스트
            sort(m,e) #오른쪽 리스트
            merge(s,m,e)
    
    def merge(s,m,e):
        temp = []; ls,rs = s,m
        while ls < m and rs < e: #두 리스트 비교 및 정렬
            if L[ls] < L[rs]:
                temp.append(L[ls])
                ls += 1
            else:
                temp.append(L[rs])
                rs += 1
        
        while ls < m:
            temp.append(L[ls])
            ls += 1
        while rs < e:
            temp.append(L[rs])
            rs += 1
        
        for i in range(s,e):
            L[i] = temp[i-s]
    
    return sort(0,len(n))

sorting = Merge_Sort(n)

for i in range(len(n)):
    print(n[i])