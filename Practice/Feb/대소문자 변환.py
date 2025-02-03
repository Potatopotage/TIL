#  문자열 s가 주어지면, 대문자는 소문자로, 소문자는 대문자로 변환하는 함수를 작성하세요.

def swap_case(s):
    swap_result = s.swapcase()
    return swap_result

# 테스트 코드
print(swap_case("Hello World"))  # "hELLO wORLD"
print(swap_case("Python"))  # "pYTHON"
