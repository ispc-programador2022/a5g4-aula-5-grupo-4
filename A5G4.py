#Menu principal
import os
import sys
import time
from turtle import clear


# ------------------------------------------------------ Funciones principales -----------------------------------------------
def tiempo():
    time.time()


opcion = 1

def nodisp():
    print("")
    print('Por el momento la funcion elegida no se encuentra disponible')
    print("")

def menu():
    if opcion != 24: # si la opción es distinta de 24 mostrar menu
        clear
        print ('------------------- Menu de Funciones -------------------------\
            \n 1- función suma, retorna la suma de 2 parámetros. \
    \n 2- función resta, retorna la resta de 2 parámetros.\
    \n 3- función producto, retorna el producto de 2 parámetros.\
    \n 4- función cociente, retorna el cociente de 2 parámetros.\
    \n 5- función módulo, retorna el módulo de 2 parámetros. \
    \n 6- función potencia, retorna la potencia del primero elevado al segundo parámetros.\
    \n 7- función radicación, retorna la raiz del primero respecto del segundo parámetros.\
    \n 8- función p1, retorna el producto de los 2 primero más el 3er parámetros, usando las funciones anteriores.\
    \n 9- función p1, retorna la suma de los 2 primero por el 3er parámetros, usando las funciones anteriores.\
    \n 10- función p1, retorna la resta de los 2 primero por el 3er parámetros, usando las funciones anteriores\
    \n 11- función genrnd que retorna una lista con 50 números aleatorios.\
    \n 12- función que devuelva la suma de las combinaciones posibles de los números generados por la función genrnd tomados de a dos.\
    \n 13- función que devuelva el producto de las combinaciones posibles de los números generados por la función genrnd tomados de a dos. \
    \n 14- función que devuelva el producto de las combinaciones posibles de los números generados por la función genrnd tomados de a dos.\
    \n 15- función que calcule la media del vector obtenido en genrnd. \
    \n 16- función que calcule la mediana del vector obtenido en genrnd. \
    \n 17- función que calcule el rango del vector obtenido en genrnd. \
    \n 18- función que calcule la varianza del vector obtenido en genrnd.\
    \n 19- función que calcule devuelva el mínimo del vector obtenido en genrnd. \
    \n 20- función que calcule devuelva el máximo del vector obtenido en genrnd.\
    \n 21- función genrnd que retorna una lista con 500.000.000.000.000.000 números aleatorios.\
    \n 22- medir el tiempo de ejecución del 16 al 20\
    \n 23- medir el tiempo de ejecución del 21 y 22 \
    \n Para salir del programa ingrese el nro 24')

    
menu() # Llamado al menu
opcion = int(input('Elija el nro de la función a ejecutar \n'))

# -------------------- Opciones disponibles por el momento ---------------------------
if opcion == 1:
    #Act1()
    nodisp()
    time.sleep(5)
    menu()

elif opcion == 2:
    #Act2()
    nodisp()
    time.sleep(5)
    menu()

elif opcion == 3:
    #Act3()
    nodisp()
    time.sleep(5)
    menu()

elif opcion == 4:
    #Act4()
    nodisp()
    time.sleep(5)
    menu()

elif opcion == 5:
    #Act5()
    nodisp()
    time.sleep(5)
    menu()

elif opcion == 21:
    star21= tiempo()
    #Act21()
    nodisp()
    end21 = tiempo()
    fin21 = end21 - star21
    print(fin21)
    time.sleep(5)
    menu()


elif opcion == 22:
    star22 = tiempo()
    #Act22()
    nodisp()
    end22 = tiempo()
    fin22 = end22 - star22
    print (fin22)
    time.sleep(5)
    menu()

elif opcion == 23:
    print("El tiempo de ejecución de las funciones 21 y 22 es de: ")
    time.sleep(15)
    menu()

elif opcion == 24:
    print ("Saliendo del programa ...")
    time.sleep(2)
    exit

else:
    print ("Número de funcion no existente...")
    time.sleep(5)
    exit


