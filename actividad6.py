print("Actividad 6")
print("Función potencia: Retorna la potencia del primero elevado al segundo parámetro")

def funcion_potencia(num1, num2):
    return num1**num2

num1 = int(input("Ingrese un primer número: "))
num2 = int(input("Ingrese un segundo número: "))

print ("La potencia es: ", funcion_potencia(num1,num2))