def gcd(a, b):
    if(b == 0):
        return a
    else:
        return gcd(b, a % b)


arr = [15, 30, 10]
A = arr[0]
for i in arr[1:]:
    A = gcd(A, i)

print(A)
