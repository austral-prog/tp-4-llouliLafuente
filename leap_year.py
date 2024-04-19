def leap_year():
    año = int(input("ingrese un año: "))
    if año %400 == 0 or (año %100 !=0 and año %4 == 0):
        print("el año " + str(año) + " es bisisto")
    else:
        print("el año " + str(año) + " no es bisisto")

leap_year()
