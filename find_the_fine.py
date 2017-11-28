T = int(input())
for i in range(T):
    N, D = map(int, input().split())
    arr = [int(x) for x in input().split()]
    arr1 = [int(x) for x in input().split()]
    penalty = 0
    if D % 2 == 0:
        for j in range(len(arr)):
            if arr[j] % 2 != 0:
                penalty += arr1[j]
    else:
        for j in range(len(arr)):
            if arr[j] % 2 == 0:
                penalty += arr1[j]
    print(penalty)
