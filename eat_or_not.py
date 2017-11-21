N = int(input())
for i in range(N):
    A = input()
    S = "SUVO"
    T = "SUVOJIT"
    count1 = A.count(T)
    count = A.count(S)
    count = count - count1
    print("SUVO = {0}, SUVOJIT = {1}".format(count, count1))
