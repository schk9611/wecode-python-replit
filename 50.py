def get_occurrence_count(my_list):
    # 함수를 완성해 주세요.
    my_dict = {}
    for i in my_list:
        my_dict[i] = my_list.count(i)
    return my_dict


print(get_occurrence_count(["one", 2, 3, 2, "one"]))
