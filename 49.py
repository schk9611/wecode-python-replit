# find_smaller_integer_divisor 라는 이름의 함수를 구현하자.
# find_smaller_integer_divisor 함수는 하나의 parameter를 받는다.
# parameter 값은 integer만 주어진다.
# find_smaller_integer_divisor 주어진 parameter 값을 나눌 수 있는 1을 제외한 "최소의 양의 정수"를 return하자.

# 예제 : find_smallest_integer_divisor(15) == 3

def find_smallest_integer_divisor(num):
    # 아래 코드를 입력해주세요.
    com = 2
    while True:
        if num % com == 0:
            return com
        else:
            com += 1


find_smallest_integer_divisor(15)
