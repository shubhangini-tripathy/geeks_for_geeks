arr = [2, 3, 4, 1, 8, -2, -3, 0, 2, 5, 4, 6, 1]
S = 5
# for i in range(len(arr)):
#     for j in range(i + 1, len(arr)):
#         if arr[i] + arr[j] == S:
#             print(arr[i], arr[j])

result = [[]]
for item in arr:
    for item2 in result:
        item2.append(item)
        if sum(item2) == S:
            print(item2)
    result.append([])