N = int(input())
A = list(input())
i = len(A) - 1
while i > 0:
    if A[i] >= A[i-1]:
        A.pop(i-1)
    i -= 1
print("".join(A))


