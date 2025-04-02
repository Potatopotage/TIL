"""
어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행
단, 두 번째 연산은 N이 K로 나누어떨어질 때만 선택 가능

1. N에서 1을 뺸다
2. N을 K로 나눈다

N이 1이 될 때까지 1번 혹은 2번 과정을 수행해야 하는 최소 횟수를 구하는 프로그램을 작성
"""

N, K = 27, 5

cnt = 0
while True:
    target = (N//K) * K
    cnt += N - target
    N = target

    if N < K:
        break
    cnt += 1
    N //= K

cnt += (N - 1)
print(cnt)
