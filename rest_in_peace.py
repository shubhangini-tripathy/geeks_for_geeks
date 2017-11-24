A = int(input()
for i in range(A):
    s = input()
    if ('21' in s) or (int(s))%21==0:
        print("The streak is broken!")
    else:
        print("The streak lives still in our heart!")
