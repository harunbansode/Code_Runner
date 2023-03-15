for t in range(int(input())):
    X, Y, A = map(int, input().split(' '))

    if A < Y:
        if A >= X:
            print('Yes')
        else:
            print('No')
    else:
        print("No")