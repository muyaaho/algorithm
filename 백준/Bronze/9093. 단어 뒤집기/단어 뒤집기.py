for _ in range(int(input())):
    a = input()
    for x in a.split():
        print(x[::-1], end=' ')
    print()