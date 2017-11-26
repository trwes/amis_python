x = float(input("Введіть х:"))
def function(x):
    '''
    Призначена для розрахунку функції, залежно від х
    Args:
    x:float, основний аргумент
    Returns:
    float, функція в даній точці
    Raises:
    -
    Examples:
    >>>print(function(-56373))
    4
    >>>print(function(3))
    9
    '''
    if 0<=x<=3:
        result = x**2
    elif x > 3 or x < 0:
        result = 4
    return result
print(function(x))
