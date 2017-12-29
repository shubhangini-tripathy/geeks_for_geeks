n = int(raw_input())
start, end = [], []
for m in range(n):
    i, j, k, l = map(int, raw_input().split())
    start.append((i, j))
    end.append((k, l))
start.sort()
end.sort()


x, y = 0, 0
count, result = 0, 0
while max(x, y) < len(end):
    i, j = start[x]
    k, l = end[y]
    if start[x] < end[y] or ((i * 60 + j) - (k * 60 + l) < 5):
        x += 1
        count += 1
    else:
        y += 1
        count -= 1
    result=max(result, count)
print(result)
