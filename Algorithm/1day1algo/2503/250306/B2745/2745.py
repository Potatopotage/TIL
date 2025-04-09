import sys
input = sys.stdin.readline

num, B = input().split()

B = int(B)

# 각 자리 숫자에 대한 정보
num_system_dict = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '09': 9,
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
    'G': 16,
    'H': 17,
    'I': 18,
    'J': 19,
    'K': 20,
    'L': 21,
    'M': 22,
    'N': 23,
    'O': 24,
    'P': 25,
    'Q': 26,
    'R': 27,
    'S': 28,
    'T': 29,
    'U': 30,
    'V': 31,
    'W': 32,
    'X': 33,
    'Y': 34,
    'Z': 35
}

# 입력값의 각 자리수를 따로 저장
num_lst = []
# 각 값에 해당하는 수 저장
for i in num:
    num_lst.append(i)

# 역순으로 계산하기 위해 뒤집기
num_lst.reverse()

dex_num = 0
# 각 자리수에 대한 10진수 계산하여 더하기
# 역순이기 때문에 0부터 시작하여 증가하는 값을 곱해준다
for j in range(len(num_lst)):
   dex_num += num_system_dict[num_lst[j]] * (B ** j)

print(dex_num)