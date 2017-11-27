N = int(input())
for i in range(N):
    T = int(input())
    arr = [int(x) for x in input().split()]
    for j in range(len(arr)):
        if arr.count(arr[j]) > 0:
            arr[j] = arr.count(arr[j])
    arr = set(arr)
    print(max(arr)- min(arr))

        
