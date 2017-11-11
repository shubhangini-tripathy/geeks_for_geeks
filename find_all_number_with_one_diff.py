max_num = 90
num = 1

while True:
    if num > 1:
        result1 = num * 10 + num - 1
        if result1 > max_num:
            break
        print(result1)

    result2 = num * 10 + num + 1
    if result2 > max_num:
        break
    print(result2)
    num += 1
