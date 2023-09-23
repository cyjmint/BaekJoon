k,n = map(int,input().split())
num = [int(input()) for _ in range(k)]

def maxlength(arr,need):
    start = 1; end = max(arr)+1
   
    while end > start+1:
        mid = (start+end)//2
        cnt = 0
        for i in range(k):
            x = arr[i]//mid
            cnt += x
        if cnt >= need:
            start = mid
        else:
            end = mid
    
    return start

print(maxlength(num, n))