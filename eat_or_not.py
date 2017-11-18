t = int(input())
for i in range(t):
    str1 = input()
    result = []
    result.append(str1[0])
    for j in range(1,len(str1)):
        if str1[j] not in result:
            result.append(str1[j])
    print(''.join(result))


    
