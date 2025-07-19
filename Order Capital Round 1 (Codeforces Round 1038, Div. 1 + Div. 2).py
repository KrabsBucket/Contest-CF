t = int(input())

for _ in range(t):
    n, m = map(int, input( ).split())

    if (n or m) == 1:
        print('NO')

    elif (n and m) == 2:
        print('NO')

    else:
        print('YES')
