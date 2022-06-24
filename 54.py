# 왼쪽 상단에 코드를 수정하셔서 scope_test 함수에 parameter 값에 상관없이 무조건 63이 return 되도록 수정하자.

# 다음 예시와 같이 되어야 한다.
# scope_test(10) == 63
# scope_test(20) == 63
# scope_test(333) == 63

def scope_test(what_is_my_scope):
    # 여기에 코드를 작성해주세요.
    def inner_scope_test(what_is_my_scope):
        # what_is_my_scope를 local 범위에서 지정해 63이 출력되도록 정의합니다.
        what_is_my_scope = 63
        return what_is_my_scope  # local 범위의 값을 가장 우선으로 가지기 때문에 63을 return합니다.
    return inner_scope_test(what_is_my_scope)
