# arr = [4,3,2,6]
arr = [9 ,6 ,5 ,7 ,8]
arr.sort()
for i in range(len(arr)):
    if len(arr) > 1:
        arr[0] = arr[0] + arr[1]
        arr.pop(1)
        arr.sort()
print(arr[0])



