x,y,w,h = list(map(int,input().split()))
print(min(min(w-x,h-y),min(x-0,y-0)))
