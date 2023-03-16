for i in range(int(input())):
    X, Y = map(int, input().split())
    if X > Y: 
        invest = X - Y
        print(invest)
    else:
        print('No Taxes')