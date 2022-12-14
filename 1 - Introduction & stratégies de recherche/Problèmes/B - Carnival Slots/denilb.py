def solve(f):
    for _ in range(int(f.readline())):
        r, c = map(int,f.readline().split())
        balls = list(map(int,f.readline().split()))
        rows = [f.readline().rstrip('\n') for _ in range(r)]

        scores = [[0] * c for _ in range(r + 1)]
        for i, sc in enumerate(map(int,f.readline().split())):
            scores[r][i] = sc

        for i in range(r-1,-1,-1):
            for j in range(c):
                if rows[i][j] == '.':
                    scores[i][j] = scores[i + 1][j]
                else:
                    mx = 0
                    for slot in (j-1, j, j+1):
                        if 0 <= slot < c:
                            mx = max(mx, scores[i + 1][slot])
                    scores[i][j] = mx
            
        print(sum(balls[i] * scores[0][i] for i in range(c)))

with open('balls.in') as f:
    solve(f) 
