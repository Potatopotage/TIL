"""
소설의 모든 장을 쓰고 나서는 각 장이 쓰여진 파일을 합쳐서 최종적으로 완성본이 들어이쓴 한 개의 파일을 만든다
이 과정에서 두 개의 파일을 합쳐서 하나의 임시파일을 만들고, 이 임시파일이나 원래의 파일을 계속 두개씩 합쳐서
소설의 여러 장들이 연속이 되도록 파일을 합쳐나가고, 최종적으로는 하나의 파일로 합친다.

두 개의 파일을 합칠 때 필요한 비용이 두 파일 크기의 합이라고 가정할 때, 최종적인 한 개의 파일을 완성하는데 필요한 비용의 총 합을 계산하시오
"""

import sys
sys.stdin = open('111066.txt', 'r')


import heapq


T = int(input())

for _ in range(T):
    K = int(input())
    files = list(map(int, input().split()))

    heapq.heapify(files)
    total_cost = 0

    while len(files) > 1:
        a = heapq.heappop(files)
        b = heapq.heappop(files)
        cost = a + b
        total_cost += cost
        heapq.heappush(files, cost)

    print(total_cost)
