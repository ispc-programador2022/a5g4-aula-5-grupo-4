#Función que devuelva el producto de las combinaciones posibles de los nros. generados por la función 
#genrnd tomados de a dos.

def prodgenrndm(numeros):
    producto = 1
    for list in numeros:
        producto *= list
    return producto

print(prodgenrndm(aleatorios)) #la variable aleatorios proviene del menu, que a su vez proviene de la función 12