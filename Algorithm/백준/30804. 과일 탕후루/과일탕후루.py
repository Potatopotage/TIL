import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    fruit_num = int(input())
    fruits = list(map(int, input().split()))
    N = len(fruits)

    queue = deque(fruits)
    print(queue)

    #앞에서 뺄 과일 a개, 뒤에서 뺄 과일 b개인데 빼다가 남은 과일이 2개가 되는 순간 끝,,, 인데
    # 우선 a, b를 정해보자

    for i in range(N - 1):
        for j in range (N - i):
            print(i, j)
            queue = deque(fruits)
            # fruit_category = set()
            for _ in range(i):
                print(queue.popleft())
            for _ in range(j):
                print(queue.pop())








"""
4
3
2
"""