N,K = map(int,input().split())
n = list(map(int,input().split()))
a = []
def merge_sort(arr):
    
    def sort(low, high):
        if low >= high:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid+1, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        i, j = low, mid+1
        while i <= mid and j <= high:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
                
        while i <= mid:
            temp.append(arr[i])
            i += 1
        while j <= high:
            temp.append(arr[j])
            j += 1
        
        i = low
        while i <= high:
            arr[i] = temp[i-low]
            a.append(temp[i-low])
            i += 1
            
    return sort(0, len(arr)-1)

sorted = merge_sort(n)
if K > len(a):
    print(-1)
else:
    print(a[K-1])