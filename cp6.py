while  D==a*b/2,:
    d=int(input( "меню\n 1-Плошадь треугольника \n 2-плошадь круга \n Выбирайте:"))

    if d == 1 :
        m=int(input( "Далее\n 1-Плошадь треугольника \n 2-периметр треугольника \n Выбирите:"))
        if m == 1:
        a = int(input("first: "))
        b = int(input("second: "))
        D=a*b/2
        print("S =", str(D),)
        if m == 2:
        v = int(input("first: "))
        g = int(input("second: "))
        C =v + g + (v**2+g**2)**0.5
        print("P=", str(C))

    if d == 2 :
        r = int(input("radius: "))
        print("S =", 3.14159265359*r**2)