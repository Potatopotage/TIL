"""
N개의 정수로 이루어진 배열 A가 주어진다
이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최대값을 구하는 프로그램을 작성하시오
|A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|
"""
import itertools
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))

def abs_sum(arr):
    sum_abs = 0
    for i in range(N - 1):
        sum_abs += abs(arr[i] - arr[i - 1])
    return sum_abs

sum_lst = []
for arr in itertools.permutations(A):
    sum_lst.append(abs_sum(arr))

print(max(sum_lst))


"""
62
"""