arr = [int(x) for x in input().split()]
num1 = int(input())
num2 = int(input())
i, j = 0, len(arr) - 1

while arr[i] != num1:
    i += 1
while arr[j] != num2:
    j -= 1

print(0 if j - i <= 1 else j - i - 1)

# for i in range(len(arr)):
#     while arr[i] != num1:
#         arr.pop(i)
#     else:
#         break
# for j in range(-1, len(arr)):
#     while len(arr) > 0 and arr[j] != num2:
#         arr.pop(j)
#     else:
#         break
# if len(arr) > 0:
#     print(0 if len(arr) - 2 <= 0 else len(arr) - 2)
