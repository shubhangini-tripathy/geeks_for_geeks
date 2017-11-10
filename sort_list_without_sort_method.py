A = [0,1,1,0,0,1,0,1,1,1,0,0,0]
B = []
C = []
for i in range(len(A)):
    if A[i]==0:
        B.append(A[i])
    else:
        C.append(A[i])
print(B+C)