# def everse(a):
#     str = ""
#     for i in a:
#         str = i + str
#     return str

# a = "42hertz"

# print("the reversed string is:",end="")
# print(reversed(a))

# 
a = "42hertz"
i = len(a) - 1

while i > -1:
    print(a[i],end = "")
    i-=1
