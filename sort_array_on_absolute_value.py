arr = [3, -7, 6, -2, - 10, 4]

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if abs(arr[i]) > abs(arr[j]):
            arr[i], arr[j] = arr[j], arr[i]
print(arr)
