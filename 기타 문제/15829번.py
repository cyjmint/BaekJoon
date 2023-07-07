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

#l = 5
#H = i : 0~4까지의 ai*r^i의 합을 M으로 나눈 나머지

#H(5) = H(4) + hash(4)
#H(4) = H(3) + hash(3)
#H(3) = H(2) + hash(2)
#H(2) = H(1) + hash(1)
#H(1) = hash(0)

#hash(n) = an*r^n