N = int(input())
for k in range(N):
    P = int(input())
    Q = [int(x) for x in input().split()]
    Z = []
    for i in range(len(Q)):
        A = i * Q[i]
        for j in range(i + 1, len(Q)):
            B = j * Q[j]
            if A > B:
                Z.append((Q[i], Q[j]))
    # print(Z)
    print(len(Z))
