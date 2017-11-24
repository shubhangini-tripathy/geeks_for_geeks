B = int(input())
for i in range(B):
    N, K, M = map(int, input().split())
    arr = []
    for j in range(N):
        A = input()
        arr.append(A)
    arr.sort(key=lambda x: x[:M])
    print(arr[K - 1])
