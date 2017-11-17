t = int(input())
for k in range(t):
    t = int(input())
    arr = [int(x) for x in input().split()]
    timei, timej = 0, 0
    counti, countj = 0, 0
    i, j = 0, len(arr) - 1
    while i <= j:
        timei += arr[i] / 2
        counti += 1
        i += 1
        while timej < timei and i <= j:
            timej += arr[j]
            countj += 1
            j -= 1

    print(counti, countj)
    if counti == countj:
        print("Tie")
    elif counti > countj:
        print("Motu")
    else:
        print("Patlu")
