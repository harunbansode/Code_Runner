T = int(input('Test Case: '))

for i in range(T):
    X, Y = input().split()
    if int(X+Y) <= 6:
        print("NO")
    else:
        print('YES')