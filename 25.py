# x값을 구해보자.

# ax = b

# 출력은 다음과 같아야 한다.
# 1. Input으로 주어진 a 와 b 값으로 위의 방정식을 충족하는 단 하나의 정수가 존재한다면 해당 정수를 출력
# 2. 만일 a 와 b 값으로 위의 방정식을 충족하는 정수가 없다면 "No Solution"을 출력
# 3. a 와 b 값으로 위의 방정식을 충족하는 정수가 많다면 "Many Solutions"을 출력

# 예시
# 만일 a = 1, b = -2 라면 결과값으로 -2가 출력되어야 한다.
# 만일 a = 2, b = -1 라면 결과값으로 "No Solution"이 출력되어야 한다.

# 풀이

a = int(input("첫번째 정수"))
b = int(input("두번째 정수"))

if a == 0:  # a가 0일 경우
    if b == 0:  # a와 b가 둘다 0일 경우
        print("Many Solutions")
    else:  # a만 0이고 b는 0이 아닌 정수인 경우
        print("No Solution")
else:  # a가 0이 아닌 정수인 경우
    if b == 0:  # a가 0이 아닌 정수이고 b가 0인 경우
        print("Many Solutions")
    else:  # a가 0이 아닌 정수이고 b가 0이 아닌 정수인 경우
        if b % a == 0:  # b/a 했을 때 나머지가 0인 경우
            print(b//a)
        else:  # b/a 했을 때 나머지가 0이 아닌 경우
            print("No Solution")
