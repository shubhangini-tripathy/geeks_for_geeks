N= int(input())
for i in range(N):
    g= int(input())
    c = [int(x) for x in input().split()]
    c.sort()
    d = []
    s = []
    for j in range(len(c)):    
        if j % 2 ==0:
            d.append(c[j])
        else:
            s.append(c[j])
    a= int("".join(str(x) for x in d))
    b= int("".join(str(x) for x in s))
    print(a+b)
    
    
    


