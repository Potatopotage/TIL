"""
5x5 빙고 판이 주어지고,
숫자 N개가 불릴 때마다 해당 숫자가 판에서 지워진다고 가정할 때,
빙고가 몇 줄 완성되었는지 출력하는 프로그램을 작성하세요.

입력 예시:
5 10 7 16 2
14 3 8 9 20
6 1 12 13 18
21 4 11 17 15
19 22 23 24 25
7
1 2 3 4 5 6 7

출력 예시:
0

"""

arr = [[5, 10, 7, 16, 2],
       [5, 3, 8, 9, 20],
       [6, 1, 12, 13, 18],
       [3, 4, 11, 17, 15],
       [6, 22, 23, 24, 25]]

N = 5
erase_num = 7
erase_lst = [1, 2, 3, 4, 5, 6, 7]

# 가로/세로 대각선이 모두 지워지면 빙고
# 모두 지운 다음에 빙고를 세야겠다

# arr의 각 요소에 들어가서 거기서 erase_list에 들어가서 일치한다면 0으로 바꾸는 것으로

for r in range(5):
    for c in range(5):
        if arr[r][c] in erase_lst:
            arr[r][c] = 0

# 이제 0들이 된 빙고판이 나왔어요 그런데,,, 여기서 어케할지 생각해봅시다

# 일단 빙고를 세 줄 변수
count_bingo = 0

# row 우선 탐색
for row in arr:
    if sum(row) == 0:
        count_bingo += 1

# column을 탐색할꺼야잉
# 아 거꾸로 뒤집어보자
arr_verse = list(map(list, zip(*arr)))
for row_reverse in arr_verse:
    if sum(row_reverse) == 0:
        count_bingo += 1

# 대각선을 탐색해봅시다
diag_sum1 = 0
for i in range(5):
    diag_sum1 += arr[i][i]

if diag_sum1 == 0:
    count_bingo += 1

diag_sum2 = 0
for i in range(5):
    diag_sum2 += arr[i][4 - i]

if diag_sum2 == 0:
    count_bingo += 1

print(count_bingo)