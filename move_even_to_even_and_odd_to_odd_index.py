# arr = [3, 5, 7, 6, 9, 10, 12, 13, 15, 16, 8, 6]
# arr1 = []
# arr2 = []
# arr3 = []
# for i in range(len(arr)):
#     if arr[i] % 2 == 0:
#         arr1.append(arr[i])
#     else:
#         arr2.append(arr[i])

# for i in range(len(arr1)):
#     arr3.append(arr1.pop(0))
#     arr3.append(arr2.pop(0))
# print(arr3)

arr = [3, 5, 7, 6, 9, 10, 12, 13, 15, 16, 8, 6]
i, j = 0, 1

while i < len(arr):
    if arr[i] % 2 != 0:
        while arr[j] % 2 != 0:
            j += 2
        arr[i], arr[j] = arr[j], arr[i]
    i += 2
print(arr)
