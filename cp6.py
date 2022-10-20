d=int(input( "меню\n 1-Плошадь треугольника \n 2-плошадь круга \n Выбирайте:"))

if d == 1 :
    a = int(input("first: "))
    b = int(input("second: "))
    D=a*b/2
    C =a + b + (a**2+b**2)**0.5
print("S =", str(D), "P=", str(C))

if d == 2 :
    r = int(input("radius: "))
print("S =", 3.14159265359*r**2)