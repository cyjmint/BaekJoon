n = int(input())
num = list(map(int,input().split()))
m = int(input())
target = list(map(int,input().split()))

def BinarySearch(num,target):
    start = 0; end = len(num)-1
    
    while start <= end:
        index = (start + end)//2
        
        if num[index] == target:
            return 1
        
        elif num[index] > target:
            end = index - 1
        
        elif num[index] < target:
            start = index + 1

    if start > end:
        return 0   

def merge_sort(arr):
    def sort(start, end):
        if end - start < 2:
            return
        mid = (start + end)//2
        sort(start,mid)
        sort(mid,end)
        merge(start,mid,end)
    
    def merge(start,mid,end):
        temp = []
        l = start; h = mid
        
        while l < mid and h < end:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1
        
        while l < mid:
            temp.append(arr[l])
            l += 1
        
        while h < end:
            temp.append(arr[h])
            h += 1
            
        for i in range(start,end):
            arr[i] = temp[i-start]
    
    return sort(0,len(arr))
        
merge_sort(num)

for i in range(m):
    print(BinarySearch(num, target[i]))