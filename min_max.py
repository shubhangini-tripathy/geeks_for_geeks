N = int(input())
arr = [int(x) for x in input().split()]
arr.sort()
a = sum(arr)
print(a - arr[0], a - arr[1])
