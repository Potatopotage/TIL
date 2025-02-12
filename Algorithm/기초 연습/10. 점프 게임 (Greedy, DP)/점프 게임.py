"""
길이가 N인 리스트 arr가 주어짐.
각 인덱스의 값은 해당 위치에서 최대로 점프할 수 있는 거리를 의미함.
0번 인덱스에서 시작하여 N-1번 인덱스에 도달하는 최소 점프 횟수를 구하라.
만약 도달할 수 없다면 -1을 출력한다.

입력 예시:
N = 5
arr = [2, 3, 1, 1, 4]

출력 예시:
2
"""
N = 5
arr = [2, 3, 1, 1, 4]

# 해당 해당 요소만큼 짬푸
# 점프 수 카운트
jump_num = 0
max_distance = 0
# max_distance + 1... ??

while max_distance < N:
    for i in range(1, arr[max_distance] + 1):
        idx = max_distance + i
        if idx < N:
            jump_distance = arr[idx] + max_distance
            max_distance = max(max_distance, jump_distance)
            jump_num += 1

print(jump_num)