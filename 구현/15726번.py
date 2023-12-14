a,b,c = map(int,input().split())
print(max(int((a/b)*c),int((a*b)/c)))
#소수점 아래를 버린다 => 모든 계산을 끝낸 후 결과값의 소수점 아래를 버림