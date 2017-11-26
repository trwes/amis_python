a = float(input("Введіть а:"))
b = float(input("Введіть b:"))
c = float(input("Введіть c:"))
def counter(a,b,c):
    '''
    Призначена для підрахунку негативних, серед 3 чисел
    Args:
    a:float, 1 з чисел
    b:float, 2 з чисел
    c:float, 3 з чисел
    Returns:
    float, що дорівнює кількості від`ємних чисел
    Raises:
    -
    Examples:
    >>>print(counter(-1,4,2))
    1
    >>>print(counter(-1,-2,-5))
    3
    '''
    count = 0
    if a < 0:
        count = count+1
    if b < 0:
        count = count+1
    if c < 0:
        count = count+1
    return count
print(counter(a,b,c))
    
