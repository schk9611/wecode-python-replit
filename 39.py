# Input으로 주어진 리스트에서 홀수는 전부 지우고 짝수만 남은 리스트를 리턴하자.
# 리스트의 요소들은 전부 숫자값이고 총 요소 수는 5개 입니다.

# 예시
# input = [1, 2, 3, 4, 5]
# 결과
# [2, 4]

def remove_odd_numbers(numbers):
    # 여기에 코드를 작성해주세요.
    for i in numbers[:]:  # for 문이 순환할 리스트를 지정할 때 슬라이싱을 통해 numbers를 복사한 리스트를 순환한다
        if i % 2 != 0:  # 홀수 지우기
            numbers.remove(i)
    return numbers  # 리턴


test1 = [1, 3, 9, 13, 5]
test2 = [1, 2, 3, 4, 5]
test3 = [3, 5, 4, 11, 20]
print(remove_odd_numbers(test1))
print(remove_odd_numbers(test2))
print(remove_odd_numbers(test3))
