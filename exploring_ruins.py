s = input()
A = list(s)
for i in range(len(A)):
    if A[i] == "?":
        if i > 0 and A[i - 1] == "a":
            A[i] = "b"
        elif i + 1 < len(A) and A[i + 1] == "a":
            A[i] = "b"
        else:
            A[i] = "a"
print(''.join(A))
