"""
판에는 4개의 자석이 놓여있고, 각 자석은 8개의 날을 가지고 있다
자석의 날바다 N극 또는 S극의 자성을 가지고 있다
4개의 자석은 1번부터 4번까지 판에 일렬로 배치되어 있고,
빨간 화살표 위치에 날 하나가 오도록 배치되어 있다

규칙
임의의 자석을 1칸씩 K번 회전시키려고 해보니,
하나의 자석이 1칸 회전될 때,
붙어있는 자석은 서로 붙어있는 날의 자성과 다를 경우에만 인력에 의해 반대 방향으로 1칸 회전된다

점수 계산
무작위로 자석을 돌렸을 때, 모든 회전이 끝난 후 아래와 같은 방법으로 점수 계산
- 1번 자석에서 빨간색 화살표 위치에 있는 날의 자성이 N극이면 0점, S극이면 1점
- 2번 자석에서 N극이면 0점, S극이면 2점
- 3번 자석에서 N극이면 0점, S극이면 4점
- 4번 자석에서 N극이면 0점, S극이면 8점

4개의 자석의 자성 정보와 자석을 1칸씩 K번 회전시키려 할 때,
K번 좌석을 회전시킨 후 획득하는 점수의 총 합을 출력하는 프로그램을 작성
"""
import sys
from pprint import pprint
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    K = int(input())
    # N극: 0
    # S극: 1
    magnetics = [list(map(int, input().split())) for _ in range(4)]
    # 시계방향 회전: 1
    # 반시계방향 회전: -1
    turn_info = [list(map(int, input().split())) for _ in range(K)]
    pprint(magnetics)

    while turn_info:
        magnetic_num, turn = turn_info.pop(0)

        if magnetic_num == 1:
            if magnetics[0][2] == magnetic_num[1][6]:
                break
            else:
                pass


    # print(turn_info)

    break






"""
#1 10
#2 14
#3 3
#4 13
#5 15
#6 10
#7 2
#8 6
#9 5
#10 4
"""