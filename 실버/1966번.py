from collections import deque

n = int(input())
for _ in range(n):
    N,M = map(int,input().split())
    paper = deque(str(i) for i in range(N))
    printer = deque(map(int,input().split()))
    target = paper[M]
    
    ans = 1
    while True:
        if any(printer[0] < printer[j] for j in range(1,N)):
            a = printer.popleft()
            b = paper.popleft()
            printer.append(a)
            paper.append(b)
        else:
            printer.popleft()
            c = paper.popleft()
            if c == target:
                print(ans)
                break
            else:
                N -= 1
                ans += 1