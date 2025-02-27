"""
첫째 줄에는 스위치 개수가 주어진다. 
스위치 개수는 100 이하인 양의 정수이다. 
둘째 줄에는 각 스위치의 상태가 주어진다. 
켜져 있으면 1, 꺼져있으면 0이라고 표시하고 사이에 빈칸이 하나씩 있다. 
셋째 줄에는 학생수가 주어진다. 
학생수는 100 이하인 양의 정수이다. 
넷째 줄부터 마지막 줄까지 한 줄에 한 학생의 성별, 학생이 받은 수가 주어진다. 
남학생은 1로, 여학생은 2로 표시하고, 학생이 받은 수는 스위치 개수 이하인 양의 정수이다. 
학생의 성별과 받은 수 사이에 빈칸이 하나씩 있다.
"""
import sys
# sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N = int(input())
switches = list(map(int, input().split()))
std_num = int(input())
for _ in range(std_num):
    order = list(map(int, input().split()))

    gender, num = order

    # 남학생의 경우
    if gender == 1:
        # 아니지 곱하고 1 빼줘야 해
        for i in range(num, N + 1, num):
            switches[i - 1] = 1 - switches[i - 1]

    if gender == 2:
        num -= 1
        if switches[num] == 0:
            switches[num] = 1
        elif switches[num] == 1:
            switches[num] = 0
        for i in range(1, N + 1):
            change_num_right = num + i
            change_num_left = num - i
            if 0 <= change_num_left < N and 0 <= change_num_right < N:
                if switches[change_num_left] == switches[change_num_right]:
                    switches[change_num_left] = 1- switches[change_num_left]
                    switches[change_num_right] = 1- switches[change_num_right]

                else:
                    break

for i in range(0, len(switches), 20):
    print(*switches[i: i + 20])



"""
1 0 0 0 1 1 0 1
"""