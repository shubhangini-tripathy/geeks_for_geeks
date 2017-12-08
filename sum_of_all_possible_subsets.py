N = int(input())
for k in range(N):
    V = input()
    sum=0
    for i in range(len(V)):
        for j in range(i,len(V)):
            sum+=int(V[i:j+1])
    print(sum)