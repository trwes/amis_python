a = input("Введіть список:").split()
n = 0
def recurtion(a,n):
    a[0+n] = a[len(a)-n]
    a[len(a)-n] = a[0+n]
    if a == a.reverse(a):
        return a
    else:
        if n != a // 2:
            n = n+1
        return recurtion(a)
print(recurtion(a,n))
