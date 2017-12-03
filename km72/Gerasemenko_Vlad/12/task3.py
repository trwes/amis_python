user_list = input("Введіть ваш список: ").split()
empty_list = []
def func(list, iterator):
    """
    Дана функція підраховує макс. послідовність однакових елементів
    Args:
        list: list
        iterator: integer number
    Returns:
        int
    Raises:
        ValueError
    Examples:
        >>>print(func([1, 1, 1, 2, 3], 0))
        3
        
        >>>print(func([1, 1, s, 2, 2, 3], 0))
        Traceback (most recent call last):
            ...
        ValueError
    """
    if iterator == len(list):
        return max(empty_list)
    list_two = "".join(list)
    count_el = list.count(list[iterator])
    if (count_el - iterator)*str(list[iterator]) in list_two:
        empty_list.append(count_el - iterator)
    return func(list, iterator + 1)
print(func(user_list, 0))
