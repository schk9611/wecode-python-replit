# greeting 함수에 적용될 decorator 함수를 구현하여 greeting 함수에 적용

# greeting 함수가 호출 되었을 때 decorator 함수에 parameter 값이 greeting 함수 리턴값의 다음에 붙혀져서 리턴되어야 한다.
# decorator 함수의 이름은 welcome_decorator 이다.

# 예를 들어,
# welcome_decorator decorator를 적용하여 greeting을 호출하면,

# @welcome_decorator
# def greeting():
#     return "Hello, "
# greeting()

# 결과값은 다음과 같아야 한다.
# "Hello, welcome to WECODE!"

def welcome_decorator(func):
    # 아래에 코드를 작성해 주세요.
    def hello():
        # hello 함수에 return 값은 출력해야한 결과값을 작성해줍니다.
        return f"{func()}welcome to WECODE!"
    return hello  # return 값으로 hello함수를 호출해 실행 시킵니다.


# decorator를 사용해 welcome_decorator 함수가 greeting이 호출되면 먼저 실행되도록 합니다.
@welcome_decorator
def greeting():
    # 아래에 코드를 작성해 주세요.
    return "Hello, "


greeting()
