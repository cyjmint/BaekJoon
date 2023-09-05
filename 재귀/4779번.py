def cantor(l,low,high):
    if high - low < 2:
        return
    gap = (high-low)//3
    mid = gap + low
    cantor(l,low,mid)
    cantor(l,mid,mid+gap)
    cantor(l,mid+gap,high)
    merge(l,mid,mid+gap)

def merge(l,mid,mid2):
    l[mid:mid2] = [' ']*(mid2-mid)

while True:
    try:
        n = int(int(input()))
        s = list('-'*3**n)
        cantor(s,0,len(s))
        print(''.join(s))
    except:
        EOFError
        break