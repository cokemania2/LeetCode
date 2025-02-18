import sys

n, m = map(int, input().split())
word_dict = {}
for i in range(n):
    word = sys.stdin.readline().rstrip()
    if len(word) < m:
        continue
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

answer = sorted(word_dict.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for v in answer:
    sys.stdout.write(v[0]+'\n')
