import sys
sys.stdin = open('input.txt', 'r')

# 방향: 북(0), 동(1), 남(2), 서(3)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def simulate(field, commands, start_r, start_c, target_r, target_c):
    direction = 0  # 항상 북쪽 시작
    r, c = start_r, start_c
    N = len(field)

    for cmd in commands:
        if cmd == 'A':
            nr = r + dr[direction]
            nc = c + dc[direction]
            if 0 <= nr < N and 0 <= nc < N and field[nr][nc] != 'T':
                r, c = nr, nc
        elif cmd == 'L':
            direction = (direction - 1) % 4
        elif cmd == 'R':
            direction = (direction + 1) % 4

    return (r, c) == (target_r, target_c)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    field = []
    start_r = start_c = target_r = target_c = -1

    for i in range(N):
        row = list(input().strip())
        field.append(row)
        for j in range(N):
            if row[j] == 'X':
                start_r, start_c = i, j
                field[i][j] = 'G'
            elif row[j] == 'Y':
                target_r, target_c = i, j
                field[i][j] = 'G'

    Q = int(input())
    results = []
    for _ in range(Q):
        parts = input().split()
        commands = parts[1]
        success = simulate(field, commands, start_r, start_c, target_r, target_c)
        results.append('1' if success else '0')

    print(f"#{tc} {' '.join(results)}")
