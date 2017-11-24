s = input()
t = []
i = int(input())
for k in range(i, len(s)):
    if s[k] == ']':
        t.pop(-1)
    elif s[k] == '[':
        t.append(s[i])
    if t == []:
        print(k)
        break