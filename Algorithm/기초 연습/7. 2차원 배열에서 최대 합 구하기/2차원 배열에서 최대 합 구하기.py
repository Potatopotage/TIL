"""
주어진 N×N 배열에서 M×M 크기의 부분 격자의 합 중 가장 큰 값을 구하세요.

입력 예시:
4 2
1 2 3 4
5 6 7 8
09 10 11 12
13 14 15 16

출력 예시:
34
"""
N, M = 4, 2
arr = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]

# 전체 배열에서 M * M 만큼 순회하여 합 더하기
# 시작 값을 왼쪽 위로 잡는다

max_sum = 0
for r in range(N - M + 1):
    for c in range(N - M + 1):
        # 각 요소에 접근
        each_sum = 0
        for v in range(M):
            for w in range(M):
                if 0 <= r + v < N and 0 <= c + w < N:
                    each_sum += arr[r + v][c + w]

        max_sum = max(each_sum, max_sum)

print(max_sum)