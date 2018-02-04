arr = [50, 8, 45, 12, 25, 40, 84]
n = 3
k = list(arr)
k.sort()
a = k[-n:]
i = 0
while i < len(arr):
    if arr[i] not in a:
        arr.pop(i)
    else:
        i += 1
print(arr)
