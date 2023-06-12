while True:
    A, B = list(map(int,input().split()))
    print('' if A==B else
          'factor' if B%A == 0 else
          'multiple' if A%B == 0 else 'neither')
    if A == 0 and B == 0:
        break

