a = input("Введіть список цілих чисел:").split()
def recurtion(a):
    a.remove(max(a))
    if len(a) == 1:
        return a
    else:
        return recurtion(a)
print(recurtion(a))
    
            
