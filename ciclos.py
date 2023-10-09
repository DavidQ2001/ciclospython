#bucle while
"""import math
numero = int(input("Digite un numero"))

while numero < 0:
    print("Error -> Deberia ser un numero positivo")
    numero = int(input("Digite un numero"))

print(f"\nSu raiz cuadrada es:{(math.sqrt(numero)):.2f}")muestra la raiz cuadrada de un numero entero positivo""" 

#el ciclo evalua una condicion y si la condicion se cumple,se ejecutaria el ciclo las bases que sean necesarias
"""i = 0 

while i < 10: imprime los numeros del 0 al 9
    print(i)
    i = i + 1"""

#bucle for se le conoce por tener un numero determinado de iteraciones
"""coleccion = {"Alejandro":34,"Maria":44,"David":22}
for clave,valor in coleccion.items(): imprime la clave y el valor del diccionario
    print(f"{clave} -> {valor}")"""

coleccion = "David" 

for i in coleccion: #imprimiendo caracter por caracter
    print(f"{i}",end = " ") #el end funciona para quitar el salto de linea