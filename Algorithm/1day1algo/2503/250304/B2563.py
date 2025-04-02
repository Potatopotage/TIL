import sys

input = sys.stdin.readline
arr = [[0] * 100 for _ in range(100)]
paper_num = int(input())
for _ in range(paper_num):
    paper = list(map(int, input().split()))
    c, r = paper

    for i in range(r, r + 10):
        for j in range(c, c + 10):
            arr[i][j] = 1

cnt = 0
for r in range(100):
    for c in range(100):
        if arr[r][c] == 1:
            cnt += 1

print(cnt)
