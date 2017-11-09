T = int(input())
for i in range(T):
    m, n, a, b = map(int, input().split())
    count = 0
    for num in range(m, n + 1):
        if num % a == 0 or num % b == 0:
            count += 1
    print(count)
