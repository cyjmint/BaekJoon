n = input().rstrip()

num = int(n,2)
o = str(oct(num))
print(int(o[2:len(o)+1]))