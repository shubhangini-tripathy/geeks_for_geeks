N = int(input())
arr = [int(x) for x in input().split()]
V = int(input())
for i in range(V):
    S = int(input())
    count = 0
    for j in range(len(arr)):
        if arr[j] < S:
            count += 1
    print(count)
