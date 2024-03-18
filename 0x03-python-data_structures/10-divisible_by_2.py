#!/usr/bin/python34
def divisible_by_2(my_list=[]):
    result = []
    for number in my_list:
        result.append(number % 2 == 0)
    return result
