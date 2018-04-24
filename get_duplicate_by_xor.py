arr = [1, 2, 3, 3, 4, 5]
result = 0

for item in arr:
    result = result ^ item

for i in range(min(arr),max(arr)+1):
    result = result ^ i

print(result)