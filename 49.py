def find_smallest_integer_divisor(num):
    # 아래 코드를 입력해주세요.
    com = 2
    while True:
        if num % com == 0:
            return com
        else:
            com += 1


find_smallest_integer_divisor(15)
