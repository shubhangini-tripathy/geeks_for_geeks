# S = input()
# B = []
# A = []
# C = []
# i = 1
# j = 0
# while i < len(S):
#     B.append(S[:i])
#     if (S[i] == S[-(i + 1)]):
#         A.append(len(B[j]))
#     i = i + 1
# print(max(A))

# I = list(input())
# count = 0
# for i in range(len(I)):
#     for j in range(len(I)):
#         if I[j] == I[]


def get_palindrom_length(arr, x, y):
    i, j = x, y
    while i < j:
        if arr[i] != arr[j]:
            return 0
        i += 1
        j -= 1
    return y - x + 1


arr = list(input())
result = 0
k, l = -1, -1
for i in range(len(arr)):
    j = len(arr) - 1
    while i < j:
        if get_palindrom_length(arr, i, j) > result:
            result = get_palindrom_length(arr, i, j)
            k, l = i, j
        j -= 1
print(''.join(arr[k: l + 1]))
