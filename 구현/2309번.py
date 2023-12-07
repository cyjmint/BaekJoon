n = [int(input()) for _ in range(9)]

#9개의 원소 중에 합이 100이 되는 7개의 원소를 찾기
x = sum(n)-100 #전체 합에서 100을 뺀 값을 합으로 하는 두 개의 원소를 찾으면 됨
for i in range(8):
    a = n[i]
    for j in range(i+1,9):
        b = n[j]
        if a+b == x: #두 원소를 찾으면 리스트에서 삭제함
            n.remove(a)
            n.remove(b)
            break 
    if len(n) == 7: #합이 100이 되는 7개의 원소를 찾으면 종료
        break

for i in range(7):
    print(sorted(n)[i])