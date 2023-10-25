people = []
sum = 0
for _ in range(10):
    a,b = map(int,input().split())
    sum -= a
    sum += b
    people.append(sum)
print(max(people))