def line():
    coeficienteA = float(input("ingrese el coeficiente A: "))
    coeficienteB = float(input("ingrese el coeficiente B: "))
    coeficienteX1 = float(input("ingrese el coeficiente X1: "))
    coeficienteX2 = float(input("ingrese el coeficiente X2: "))
    print("el coeficiente A de ecuacion de la recta es: " + str(coeficienteA))
    print("el coeficiente B de ecuacion de la recta es: " + str(coeficienteB))
    print("el coeficiente X1 de ecuacion de la recta es: " + str(coeficienteX1))
    print("el coeficiente X2 de ecuacion de la recta es: " + str(coeficienteX2))
    print("\n")
    print("para la siguiente ecucacion: ")
    print("Y =" + str(coeficienteA) + "X" + str(coeficienteB))
    print("\n")

    Y1 = (coeficienteA * coeficienteX1) + coeficienteB
    Y2 = (coeficienteA * coeficienteX2) + coeficienteB
    P1 = coeficienteX1, + Y1
    P2 = coeficienteX2, + Y2
    print("dado los siguente pusntos: ")
    print("P1" + str(P1))
    print("P2" + str(P2))
    print("\n")

    distancia = ((coeficienteX2 - coeficienteX1) **2 +(Y2 - Y1 ) ** 2) **(1/2)
    print("distancia entre ellos es: " + str(distancia))
