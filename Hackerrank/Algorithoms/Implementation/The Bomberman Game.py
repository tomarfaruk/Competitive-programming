r, c, n = map(int, input().strip().split())
if n % 2 == 0:
    for i in range(r):
        print('O'*c)
else:
    grid = [input() for i in range(r)]
    if 1==n:
        for row in grid:
            print (''.join(row))
    else:
        n /= 2
        for it in range((n + 1) % 2 + 1):
            ngrid = [['O']*c for i in range(r)]
            def setgrid(i, j, ch):
                if 0 <= i < r and 0 <= j < c:
                    ngrid[i][j] = ch
            for i in range(r):
                for j in range(c):
                    if grid[i][j] == 'O':
                        setgrid(i, j, '.')
                        setgrid(i+1, j, '.')
                        setgrid(i-1, j, '.')
                        setgrid(i, j+1, '.')
                        setgrid(i, j-1, '.')

            grid = ngrid

        for row in grid:
            print (''.join(row))