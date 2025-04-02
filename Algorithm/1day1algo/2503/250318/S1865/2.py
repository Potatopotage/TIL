"""
N의 직원이 있는 회사에 N개의 일이 생겼다

직원들에게 공평하게 일을 하나씩 배분하려고 한다
직원들의 번호가 1부터 N까지 매겨져 있고, 해야 할 일에도 번호가 1부터 N까지 매겨져 있을 때,
i번 직원이 j번 일을 하면 성공할 확률이 pi/j이다

주어진 일이 모두 성공할 확률의 최대값을 구하는 프로그램을 작성

퍼센트 단위로 소수점 아래 7번째 자리에서 반올림하여 6번재까지 출력
"""
import sys
sys.stdin = open('input.txt', 'r')

from itertools import permutations

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    A = [i for i in range(N)]

    result = []
    # 최소 생산 비용
    max_success = 0

    for per in permutations(A):
        curr_success = 1
        r = 0
        for i in range(N):
            curr_success *= (arr[r][per[i]])
            r += 1
        result.append(curr_success)

    print(max(result))



"""
#1 9.100000
"""