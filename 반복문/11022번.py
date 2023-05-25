#import sys

T = int(input())
#input = sys.stdin.readline
for i in range(T):
    A, B = list(map(int,input().split()))
    print('Case #%d: %d + %d = %d'%((i+1),A,B,A+B))