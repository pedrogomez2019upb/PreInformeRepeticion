#Ejercicio para imprimir los 15 primeros números pares  
#Aún asi vamos a intentar de que la persona pueda ingresar el numero siempre y cuando sea positivo
x=int(input("Bienvenido! Este programa te permite mostrar los 15 primeros números pares positivos de un número. Por favor ingresa el número positivo: "))
n=15
if x < 0:
    print ("El número es negativo o es 0. Muchas gracias por utilizar el programa")
else:
        while(x<=(n)):
            y=x*2
            print("Los 10 primeros valroes positivos son: {}".format(y))
            x=x+1
#Desarrollado por Pedro Gómez / ID : 000396221

