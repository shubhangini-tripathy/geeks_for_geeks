
def trailing_zeros(fact):
    fact = str(fact)
    i = len(fact) - 1
    count = 0
    while fact[i] == "0":
        count += 1
        i -= 1
    return count

T = int(input())
for j in range(T):
    N = int(input())
    fact = 1
    for i in range(1, N + 1):
        fact = fact * i
    print(trailing_zeros(fact))


