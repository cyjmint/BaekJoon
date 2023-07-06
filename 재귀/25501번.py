def recursion(s, l, r, n=0):
    if l >= r:
        return print(1, end = ' '), print(n+1)
    elif s[l] != s[r]: 
        return print(0, end = ' '), print(n+1)
    else: 
        return recursion(s, l+1, r-1, n+1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

T = int(input())
for i in range(T):
    isPalindrome(input())