N = int(input())
for i in range(N):
    T = int(input())
    arr = [int(x) for x in input().split()]
    arr.sort()
    print(arr[0] * arr[1])
