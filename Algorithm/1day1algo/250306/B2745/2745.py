import sys
input = sys.stdin.readline

num, B = input().split()

B = int(B)

num_system_dict = {
    '0': 0,
    '1': 1,
    '2': 1,
    '3': 1,
    '4': 1,
    '5': 1,
    '6': 1,
    '7': 1,
    '8': 1,
    '9': 1,
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

num_lst = []
for i in num:
    num_lst.append(i)

num_lst.reverse()

dex_num = 0
for j in range(len(num_lst)):
   dex_num += num_system_dict[num_lst[j]] * (B ** j)

print(dex_num)