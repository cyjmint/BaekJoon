import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a,b = input().rstrip().split()
    if sorted(list(a)) == sorted(list(b)): 
        #두 글자가 애너그램 관계인지 확인하기 위해서 알파벳을 정렬한 리스트가 같은지 확인
        print(f"{a} & {b} are anagrams.")
    else:
        print(f"{a} & {b} are NOT anagrams.")
#문자열 출력을 할 때는 철자가 틀리지 않았는지 꼭 확인