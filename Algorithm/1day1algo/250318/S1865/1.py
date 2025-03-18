"""
N의 직원이 있는 회사에 N개의 일이 생겼다

직원들에게 공평하게 일을 하나씩 배분하려고 한다
직원들의 번호가 1부터 N까지 매겨져 있고, 해야 할 일에도 번호가 1부터 N까지 매겨져 있을 때,
i번 직원이 j번 일을 하면 성공할 확률이 pi/j이다

주어진 일이 모두 성공할 확률의 최대값을 구하는 프로그램을 작성

퍼센트 단위로 소수점 아래 7번째 자리에서 반올림하여 6번째까지 출력
"""
import sys
sys.stdin = open('input.txt', 'r')

# 각 직원이 일을 선택하는 경우, 최대 성공률을 구하는 함수
def dfs(employee, sucess_rate):
    global max_success

    # 현재 성공률이 최대 성공률보다 작아지면 return
    if sucess_rate <= max_success:
        return

    # 모든 직원이 선택한 후 최대값 갱신
    if employee == N:
        max_success = max(max_success, sucess_rate)

    # 직원이 각 일을 선택하는 경우
    for work in range(N):
        # 선택하지 않은 일이라면
        if visited[work] is False:
            # 방문처리
            visited[work] = True
            # 다음 직원 진행
            dfs(employee + 1, sucess_rate * (arr[employee][work] / 100))
            # 방문처리 복구
            visited[work] = False

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [False] * N
    # 최대 성공률
    max_success = 0

    dfs(0, 1)

    # 소수점 6번째자리까지 출력
    print(f'#{tc} {max_success * 100:.6f}')



"""
#1 9.100000
"""