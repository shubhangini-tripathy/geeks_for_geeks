# "axyblmqbhctxxazyttqctbxa"
# a b c
A = list("axyblmqbhctxxazyttqctbxa")
B =  "a b c".split()
C = []
count = len(A)
for i in range(len(A)):
    for j in range(i, len(A)):
        if set(B).issubset(A[i:j+1]):
            if j+1-i < count:
                count = j+1-i
print(count)
        
