"""
제일 위에 있는 카드를 바닥에 버린다.
그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.

N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하시오.
"""
from collections import deque
import sys

input = sys.stdin.readline

N = int(input())

dq = deque()

for i in range(N):
    dq.append(i + 1)

while len(dq) > 1:

    dq.popleft()

    dq.append(dq.popleft())

print(*dq)


"""
4
"""