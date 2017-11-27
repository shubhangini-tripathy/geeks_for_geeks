N = int(input())
for i in range (N):
    n , k = map(int, input().split())
    arr = [int(x) for x in input().split()]
    for j in arr:
        if arr.count(j) == 1:
            print(j)

