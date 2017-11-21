# 3: fizz
# 5: buzz
# 15: fillbuzz
# else: no
for t in range(int(input())):
    i = int(input())
    print("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or str(i))
