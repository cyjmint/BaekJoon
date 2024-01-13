s = input()
stack = []
ans = ''

for i in range(len(s)):
    stack.append(s[i])
    if s[i] == '<':
        stack.pop()
        ans += ''.join(list(reversed(stack)))
        stack.clear()
        stack.append(s[i])
        continue

    if s[i] == '>':
        ans += ''.join(stack)
        stack.clear()
        continue

    if s[i] == ' ':
        if '<' in stack:
            continue
        else:
            stack.pop()
            ans += ''.join(list(reversed(stack)))
            stack.clear()
            ans += s[i]
            continue
    
    if i == len(s)-1:
        ans += ''.join(list(reversed(stack)))

print(ans)