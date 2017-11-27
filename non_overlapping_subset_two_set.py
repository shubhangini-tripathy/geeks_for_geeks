A = {1, 5, 3, 8}
B = {5, 4, 6, 7}
A = list(A)
B = list(B)
result = 0
for i in range(len(A)):
    if A[i] not in B:
        result += A[i]
    if B[i] not in A:
        result += B[i]
print(result)
# print(sum(A.union(B) - A.intersection(B)))
