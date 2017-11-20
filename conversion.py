N = int(input())
for j in range(N):
    S = input()
    s = list(S)
    for i in range(len(s)):
        if ord(s[i]) > 96:
            s[i] =str(ord(s[i]) - 96)
        elif s[i] == " ":
            s[i] = "$"
        else:
            s[i] = str(ord(s[i]) - 64)
    print(''.join(s))


        

        
