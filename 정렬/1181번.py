n = int(input())
words = set()
for _ in range(n):
    words.add(input())

words = list(words)
s_words = sorted(words)
s_words2 = sorted(s_words, key=len)

for v in s_words2:
    print(v)