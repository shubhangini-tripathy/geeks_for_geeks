A = int(input())
B = set("aeiou")
for i in range(A):
    S = input()
    count = 0
    for j in range(len(S)):
        if S[j] in B:
            count += 1
    print(count)
