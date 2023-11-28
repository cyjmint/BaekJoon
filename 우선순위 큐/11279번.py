import heapq

heap = []
n = int(input())
for i in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(heap,(-x,x))
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])