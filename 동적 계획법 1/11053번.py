n = int(input())
num = list(map(int,input().split()))
lis = [] #lis[i] : 길이가 i인 증가하는 부분 수열을 만들 수 있는 마지막 원소 중에서 가장 작은 값
lis.append(num[0])

def binary_search(start, end): #lower_bound 찾는 이진 탐색 함수
    while start < end:
        ind = (start+end)//2
        if lis[ind] < a:
            start = ind + 1
        else:
            end = ind
    return end
    
for i in range(1,n):
    a = num[i]
    if a > lis[-1]:
        lis.append(a)
    else:
        lower_bound = binary_search(0,len(lis)-1)
#lower bound : 정렬된 배열에서 어떤 값이 삽입될 수 있는 위치들 중 가장 인덱스가 작은 위치
#upper bound : lower bound의 반대
        lis[lower_bound] = a

print(len(lis))