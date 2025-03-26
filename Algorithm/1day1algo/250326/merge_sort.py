data_array = [69, 10, 30, 2, 16, 8, 31, 22]

def merge(left_arr, right_arr):
    global comparison_cnt

    if left_arr and right_arr:
        if left_arr[-1] > right_arr[-1]:
            comparison_cnt += 1

comparison_cnt = 0