x1 = int(input("Введіть рядок х1 (від 1 до 8):"))
y1 = int(input("Введіть стовпчик y1 (від 1 до 8):"))
x2 = int(input("Введіть рядок х2 (від 1 до 8):"))
y2 = int(input("Введіть стовпчик y2 (від 1 до 8):"))
if (0<x1<9)&(0<y1<9)&(0<x2<9)&(0<y2<9):
    if ((x1+y1)%2) == ((x2+y2)%2):
        print("yes")
    else:
        print("no")
else:
    print("Ви ввели невірні координати")