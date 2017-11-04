N = int(input())
for i in range(N):
    W, H = input().split()
    W, H = int(W, 2), int(H, 2)
    print(W * H)
