#import sys
#input = sys.stdin.readline
data = []
for i in range(10):
    data.append(int(input())%42)
print(len(set(data)))