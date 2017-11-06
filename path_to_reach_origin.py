def get_possible_way(m, n):
    if min(m, n) < 0:
        return 0
    if m == 0 and n == 0:
        return 1
    return get_possible_way(m - 1, n) + get_possible_way(m, n - 1)

N = int(input())
for i in range(N):
    m, n = map(int, input().split())
    print(get_possible_way(m, n))
    # arr = [(0, 0)]
    # temp = []
    # while True:
    #     for x, y in arr:
    #         if x + 1 <= m:
    #             temp.append((x + 1, y))
    #         if y + 1 <= n:
    #             temp.append((x, y + 1))

    #     if len(temp) == 0:
    #         print(len(arr))
    #         break
    #     else:
    #         arr = temp
    #         temp = []



