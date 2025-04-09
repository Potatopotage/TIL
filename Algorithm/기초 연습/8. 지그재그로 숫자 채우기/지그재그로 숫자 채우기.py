"""
N×N 크기의 격자에 숫자를 지그재그(Z 모양)로 채운 행렬을 출력하세요.

입력 예시:
4

출력 예시:
1  2  3  4
8  7  6  5
09 10 11 12
16 15 14 13
"""

# 행을 지그재그로 순회합니다

N = 4

arr = [[0] * 4 for _ in range(4)]

num = 0

for r in range(4):
    if r % 2 == 0:
        for c in range(4):
            num += 1
            arr[r][c] = num
    else:
        for c in range(3, -1, -1):
            num += 1
            arr[r][c] = num

for lst in arr:
    print(*lst)