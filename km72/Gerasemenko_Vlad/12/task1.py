a = input("Введіть список натуральних чисел:").split()
def recurtion(a):
    """
    Дана фунція знаходить 2 , після максимального елемент
    Args:
        a: list
    Returns:
        int
    Raises:
        ValueError
    Examples:
        >>>print(recurtion(1 2 3))
        2
        
        >>>print(recurtion(s))
        Traceback (most recent call last):
            ...
        ValueError
    """
    a.remove(min(a))
    if len(a) == 2:
        a.remove(max(a))
        return a
    else:
        return recurtion(a)
print(recurtion(a))

