N, M = map(int, input().split())
mat = []
for i in range(N):
    mat.append([int(x) for x in input().split()])

ones, twos = [], set()

for i in range(N):
    for j in range(M):
        if mat[i][j] == 1:
            ones.append((i, j))
        elif mat[i][j] == 2:
            twos.add((i, j))
count = 0
while len(ones) > 0:
    i = 0
    temp = set()
    while i < len(ones):
        x, y = ones[i]
        if len(
                set([(x + 1, y), (x, y + 1), (x, y - 1),
                     (x - 1, y)]).intersection(twos)) > 0:
            temp.add(ones.pop(i))
        else:
            i += 1
    count += 1
    twos = twos.union(temp)

print(count)
