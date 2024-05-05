#def union_list(list_1: list_2) ->list:
    # intersection = []
    # for i in list_1:
    #     if i in list_2:
    #         intersection.append(i)
    # return intersection


#print(union_list([1, 2, 3, 4], [3, 4, 5, 6]))

from typing import List

def uniqueness(list_1: List[int], list_2: List[int]) ->list[int]:
    """функция принимает 2 списка чисел и возврает новый только с уникальными числами"""
    return list(set(list_1) - set(list_2)) + list(set(list_2) - set(list_1))


if __name__ == '__main__':
    print(uniqueness([1, 2, 3, 4], [3, 4, 5, 6]))

    

