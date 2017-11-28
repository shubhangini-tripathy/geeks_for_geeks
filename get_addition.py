def is_inc_list(arr):
    print(arr)
    for i in range(len(arr)):
        arr[i] = arr[i] + 1
    return arr


print(is_inc_list([1,3,4]))



