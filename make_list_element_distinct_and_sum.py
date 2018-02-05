arr = [3,4,6,8]
i = 0
while i+1 < len(arr):
    if arr[i] == arr[i+1]:
        arr[i+1] += 1
    else:
        i+=1
print(sum(arr))
        

