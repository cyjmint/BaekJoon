A, B = input().split()
r_A = list(reversed(A))
r_B = list(reversed(B))
A1 = int(r_A[0]) * 100 + int(r_A[1]) * 10 + int(r_A[2])
B1 = int(r_B[0]) * 100 + int(r_B[1]) * 10 + int(r_B[2])
if A1 > B1:
    print(A1)
else:
    print(B1)