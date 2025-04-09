"""
규칙
1. 뽑고자 하는 카드가 포함되어 있는 행을 선택
2. 선택된 행에 포함된 카드 중 가장 숫자가 낮은 카드 뽑기
3. 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략
"""

import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

print(arr)

min_lst = []

for row in arr:
    min_lst.append(min(row))

print(max(min_lst))