from collections import deque

n = int(input())
card = deque(i for i in range(1,n+1))

while len(card) > 1:
    card.popleft()
    card.append(card[0])
    card.popleft()
print(*card)