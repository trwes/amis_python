a = float(input("Введіть число а:"))
n = int(input("Введіть бажану степінь:"))
def power(a,n):     # Вводиться функція
    an = 1          # Нова змінна = 1
    for i in range(n):   
            an = a*an   # Цикл перемножає а n разів
    return an
if n >= 0: 
    print(power(a,n)) # Якщо n більше 0, то парматер(n), а якщо n менше 0, то (-n)
elif n < 0:
    print("1 /",power(a,-n))   # Можна було б просто розрахувати, але це може привести до машинного 0
