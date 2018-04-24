# a = [1,2,3,2]
# b = [1,2,3,20]
# x = a+b
# print(set(x))

a = [1,2,3,2]
b = [1,2,3,20]
for i in a:
    if i in b == False:
        a.pop(i)
print(set(a))



