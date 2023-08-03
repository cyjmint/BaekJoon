n = [int(input()) for i in range(5)]
for i in range(5):
    if n[i] < 40:
        n[i] = 40
print(sum(n)//len(n))