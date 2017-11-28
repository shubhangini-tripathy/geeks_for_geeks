A = int(input())


def create_string(C, D, X, Y):
    while True:
        xcount = min(C, X)
        while xcount > 0:
            print("0", end=" ")
            xcount -= 1
        C = max(0, C - X)

        ycount = min(D, Y)
        while ycount > 0:
            print("1", end=" ")
            ycount -= 1
        D = max(0, D - Y)

        if C <= 0 and D <= 0:
            return


for i in range(A):
    X, Y = map(int, input().split())
    S = input()
    T = ""
    C = S.count("0")
    D = S.count("1")
    create_string(C, D, X, Y)
    print("")