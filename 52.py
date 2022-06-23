# 두개의 함수 구현
# ･ sum_of_numbers
# ･ what_is_my_full_name

# 함수 sum_of_numbers 는 argument로 주어지는 모든 수를 합한 값을 return 해야 한다.
# 예를들어,
# sum_of_numbers(1,2,3,4,5)는 15를 return해야하고 sum_of_numbers(1,2)는 3을 return해야한다.
# 만일 parameter가 주어지지 않으면 0을 return 해야한다.

# what_is_my_full_name 함수는 주어진 parameter 중 first_name과 last_name 이라는 parameter를 조합하여 full name을 return 해주어야 한다.
# 예를들어,
# first_name이 "우성"이고 last_name이 "정"이면 "정 우성" 라고 return한다.

# Last name과 first name 사이에 빈칸(space)이 들어가야한다.
# 만일 last_name이 없거나 first_name이 없으면 둘 중 하나만 return 하면 된다.
# 예를들어,
# last_name이 없으면 "우성"이라고 이름만 return한다.
# 마지막으로, last_name과 first_name 둘다 없으면 "Nobody"라고 return 하면 된다.

def sum_of_numbers(*args):
    # 아래에 코드를 작성해 주세요.
    sums = 0
    for i in args:
        sums += i
    return sums


def what_is_my_full_name(**kwargs):
    # 아래에 코드를 작성해 주세요.
    if "last_name" in kwargs:
        if "first_name" in kwargs:
            return kwargs["last_name"] + " " + kwargs["first_name"]
        else:
            return kwargs["last_name"]
    else:
        if "first_name" in kwargs:
            return kwargs["first_name"]
        else:
            return "Nobody"
