while True:
    print("""
    Calculadora simple RGP
    Bienvenido
    Dime, ¿qué quieres hacer?
    
    1) Sumar los dos números
    2) Restar los dos números
    3) Multiplicar los dos números
    4) Dividir entre 2 numeros
    5) Averiguar si un numero es primo
    6) Averiguar si un numero es polindromo
    7) Apagar calculadora
    """)
    opcion = int(input("Elige una opción: ") )     

    if opcion == 1:
        numero_1 = int(input("Introduce tu primer número: ") )
        numero_2 = int(input("Introduce tu segundo número: ") )
        print(" ")
        print("RESULTADO: La suma de",numero_1,"+",numero_2,"es igual a",numero_1+numero_2)
    elif opcion == 2:
        numero_1 = int(input("Introduce tu primer número: ") )
        numero_2 = int(input("Introduce tu segundo número: ") )
        print(" ")
        print("RESULTADO: La resta de",numero_1,"-",numero_2,"es igual a",numero_1-numero_2)
    elif opcion == 3:
        numero_1 = int(input("Introduce tu primer número: ") )
        numero_2 = int(input("Introduce tu segundo número: ") )
        print(" ")
        print("RESULTADO: El producto de",numero_1,"*",numero_2,"es igual a",numero_1*numero_2)
    elif opcion == 4:
        numero_1 = int(input("Introduce tu primer número: ") )
        numero_2 = int(input("Introduce tu segundo número: ") )
        print(" ")
        print("RESULTADO: La division de",numero_1,"*",numero_2,"es igual a",numero_1/numero_2)
                  
    elif opcion == 5:
        numero_1= int(input("¿Qué número desea saber si es primo? "))
        valor= range(2,numero_1)
        contador = 0
        for variable_n in valor:
          if numero_1 % variable_n == 0:
            contador +=1
            print("divisor:", variable_n)
 
        if contador > 0 :
          print("El numero no es primo" )
        else:
          print("El numero es primo")

    elif opcion == 6:
        numero_1 = input("¿Qué número desea saber si es polindromo? ") 
        if numero_1 == numero_1[::-1]: 
            print("Si es Polindromo") 
        else: 
            print("No es Polindromo")

    elif opcion == 7:
        break
    else:
        print("Opción incorrecta")
