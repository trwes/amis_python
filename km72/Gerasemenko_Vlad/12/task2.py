a = input("Введіть список чисел:").split()
counter = 0
i = len(a)-1
def recurtion(a,i,counter):
    """
    Дана фунція знаходить кількість максимальних елементів в списку
    Args:
        a: list
        counter: int
        i: int
    Returns:
        int
    Raises:
        ValueError
    Examples:
        >>>print(recurtion(1 2 3 3 3,0,0))
        3
        
        >>>print(recurtion(s,0,0))
        Traceback (most recent call last):
            ...
        ValueError
    """
    if a[i] == max(a):
        counter = counter + 1
    if i == 0:
        return counter
    if i != 0:
        return recurtion(a,i-1,counter)
print(recurtion(a,i,counter))
