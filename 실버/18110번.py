n = int(input())
score = [int(input()) for _ in range(n)]
score = sorted(score)

def round45(n):
    return int(n) + (1 if n%1 >= 0.5 else 0)

if n == 0:
    print(0)
else:
    cut = round45(n*.15)
    s = sum(score[cut:(n-cut)])
    ans = round45(s/(n-2*cut))
    print(ans)