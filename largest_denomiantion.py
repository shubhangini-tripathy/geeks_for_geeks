V = 421
result = []
C = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
C.sort(reverse=True)
i = 0
while i < (len(C)):
    while V >= C[i]:
        result.append(C[i])
        V = V - C[i]
    i += 1
print(result)
