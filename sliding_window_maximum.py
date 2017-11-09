C = [int(x) for x in input().split()]
k = int(input())
arr1 = []
for i in range(len(C) - k + 1):
    print(max(C[i:i + k]), end=' ')
