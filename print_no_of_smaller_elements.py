N = int(input())
for i in range(N):
    T = int(input())
    c = [int(x) for x in input().split()]
    Q = int(input())
    count = 0
    for j in range(len(c)):
        if c[j] <= Q:
            count += 1
    print(count)
