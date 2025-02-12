"""
N개의 숫자를 입력받아,
가장 많이 등장한 숫자를 출력하는 프로그램을 작성하세요.
(동일한 빈도의 숫자가 여러 개라면 가장 작은 값을 출력)

입력 예시:
10
1 3 2 2 4 1 3 3 2 2

출력 예시:
2

"""

# 카운팅 정렬 만들어야죠 아무래도

N = 10
arr = [1, 3, 2, 2, 4, 1, 3, 3, 2, 2]

count_list = [0] * (max(arr) + 1)

for idx in arr:
    count_list[idx] += 1

print(count_list.index(max(count_list)))