"""
아래와 같은 삼각형에서 위에서 아래로 내려가는 경로 중 최대 합을 구하세요.

입력 예시:
4
3
7 4
2 4 6
8 5 09 3

출력 예시:
23
"""

arr = [[3],
       [7, 4],
       [2, 4, 6],
       [8, 5, 9, 3]]

max_sum = 0
for c in range(len(arr[-1])):
    sum_col = 0
    for r in range(len(arr)):
        if 0 <= c < len(arr[r]):
            sum_col += arr[r][c]

    max_sum = max(max_sum, sum_col)

print(max_sum)