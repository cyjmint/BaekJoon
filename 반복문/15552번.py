#빠른 입력
#input() 대신 sys.stdin.readline()을 사용하면 반복문에서 더 빠르게 입력을 할 수 있지만, Spyder 환경에서는
#sys.stdin.readline()이 작동하지 않음. 그래서 input()으로 코드를 작성하고 백준에서 주석의 내용을 추가해서 제출함

#import sys
T = int(input())
#input = sys.stdin.readline
for i in range(T):
    A, B = list(map(int,input().split()))
    print(A+B)
    