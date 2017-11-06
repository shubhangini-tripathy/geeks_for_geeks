N = int(input())
for i in range(N):
    m, n = map(int, input().split())
    arr = [(0, 0)]
    temp = []
    while True:
        for x, y in arr:
            if x + 1 <= m:
                temp.append((x + 1, y))
            if y + 1 <= n:
                temp.append((x, y + 1))

        if len(temp) == 0:
            print(len(arr))
            break
        else:
            arr = temp
            temp = []
