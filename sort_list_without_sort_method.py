# A = [0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0]
# for i in range(len(A)):
#     for j in range(len(A) - 1):
#         if A[j] > A[j + 1]:
#             A[j + 1], A[j] = A[j], A[j + 1]
# print(A)


A = [0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0]
i, j = 0, len(A) - 1
while i < j:
    if A[i] == 1:
        while A[j] == 1:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    i += 1
print(A)
