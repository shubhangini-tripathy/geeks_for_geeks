A = [0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0]
for i in range(len(A)):
    for j in range(len(A) - 1):
        if A[j] > A[j + 1]:
            A[j + 1], A[j] = A[j], A[j + 1]
print(A)
