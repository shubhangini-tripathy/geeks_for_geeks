# N = int(input())
# B = []
# for i in range(N):
#     A = set(input())
#     B.append(A)
# count = 0
# for j in range(len(B)):
#     for k in range(j + 1, len(B)):
#         if B[j] - B[k] == set():
#             count += 1
# print(count)

str_set = set()
for i in range(int(input())):
    a = input()
    if len(a) > 3:
        a = a[0] + "".join(sorted(list(a[1:-1]))) + a[-1]
    if a not in str_set:
        str_set.add(a)
print(len(str_set))
