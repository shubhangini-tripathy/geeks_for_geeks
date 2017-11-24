arr = [5, 10, 15, 25, 30, 45, 35, 20, 40]


def my_key(item):
    if item % 15 == 0:
        return 0
    elif item % 10 == 0:
        return 1
    else:
        return 2


arr.sort(key=my_key)
print(arr)


# arr1 = []
# arr2 = []
# arr3 = []
# for i in range(len(arr)):
#     if arr[i] % 15 == 0:
#         arr1.append(arr[i])
#     elif arr[i] % 10 == 0:
#         arr2.append(arr[i])
#     elif arr[i] % 5 == 0:
#         arr3.append(arr[i])

# arr1.sort()
# arr2.sort()
# arr3.sort()
# print(arr1 + arr2 + arr3)


# i = 0
# while i < len(arr):
#     if arr[i] % 15 == 0:
#         arr.insert(app.pop(i))
#     elif arr[i] % 5 == 0 and arr[i] % 10 != 0:
#         arr.append(arr.pop(i))
#     else:
