from string import ascii_lowercase
al = list(ascii_lowercase)

L = int(input())
s = input()
M = 1234567891
r = 31

def h(n):
    return (al.index(s[n])+1)*(r**n)

def H(n):
    if n == 1:
        return h(n-1)
    else:
        return H(n-1) + h(n-1)
        
print(H(L)%M)