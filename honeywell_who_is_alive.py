N = int(input())
arr = [int(x) for x in input().split()]
i = 0
power = -float('inf')

for i in range(len(arr)):
    if arr[i] >= power:
        power = arr[i]
        print(i + 1, end=' ')


# while i < len(arr):
#     j = i + 1
#     while j < len(arr):
#         if arr[i] > arr[j]:
#             arr.pop(j)
#         else:
#             j += 1
#     i += 1
# print(i, j)
