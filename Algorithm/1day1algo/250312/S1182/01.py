"""
N개의 정수로 이루어진 수열이 있을 때,
크기가 양수인 부분 수열 중에서 그 수열의 원소의 합계가 S가 되는 경우의 수를 구하는 프로그램을 작성하시오
"""
import sys
from itertools import combinations
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
for i in range(1, len(arr) + 1):
    for comb in combinations(arr, i):
        curr_sum = sum(comb)
        if curr_sum == S:
            cnt += 1

print(cnt)


"""
1
"""