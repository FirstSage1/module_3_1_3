# Модуль 3_1 пространство имен.
# ==========================================
# calls = 0

# def count_calls():
#  global calls
# calls+=1


# cort_str_ = (0)
#
#
# def String_info(str_):  # Содание функции
#     global cort_str_  # Объявление глоальной пер. внутри функции
#     long_str_ = len(str_)
#     hi_str_ = str_.upper()
#     low_str_ = str_.lower()
#     cort_str_ = (long_str_, hi_str_, low_str_)
#
#     # global calls
#     # count_calls()
#
# string_info("Рубеж")
# print(cort_str_)
# String_info("Приход")
# print(cort_str_)


# flag_ = False
# def is_contains(string, list_to_searh):
#     global flag_
#     flag_ = string in list_to_searh
#
#     #print(string in list_to_searh)
#
# is_contains('Добр',[24,'добр','добрый'])
# print(flag_)
# is_contains('Добр',[24,'Добро','добрый'])
# print(flag_)
# global calls


def is_contains(string, list_to_searh):
    #flag_ = False
    #string = string.upper()
    # print(string)
    for i in list_to_searh:
        if string.upper()==i.upper():
            return True
        return False
    #     if type(i) == type(string):
    #         i = i.upper()
    #         # print(i)
    #     if string == i:
    #         flag_ = True
    #print()
    # return flag_
is_contains('Добр', [24, 'добр', 'добрый'])
#result_1 = is_contains('flag_')
#print(result_1)
is_contains('Добр', [24, 'Добро', 'добрый'])
#result_2 = is_contains('flag_')
#print(result_2)
#     count_calls()
#     print(is_contains)
#     calls = calls + 1
#     return ()
# print(string)
# return True or False
