# arr = [1, 7,8, 9, 10, 3, 2, 5, 6]
arr = [4, 5, 2, 3, 1]
# find minimum number not present in array and
# that number should be greater than zero
for num in range(1, max(arr) + 2):
    if num not in arr:
        print(num)
        break
# else:
#     print(max(arr)+1)
