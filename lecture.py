#ejercicio de operadore morsa
 
# Ejercicio 1: Leer números del usuario hasta que se ingrese un número negativo

numeros = []
while (numero := int(input("Ingrese un número: "))) >= 0:
    numeros.append(numero)
print("Números ingresados:", numeros)
 
 
# Ejercicio 2: Crear una lista con los cuadrados de los números pares del 1 al 10

cuadrados_pares = [numero ** 2 for numero in range(1, 11) if (numero % 2 == 0)]
print("Cuadrados de los números pares:", cuadrados_pares)
 
 
# Ejercicio 3: Verificar si un número es positivo, negativo o cero

numero = int(input("Ingrese un número: "))
if (signo := "positivo") if numero > 0 else (signo := "negativo") if numero < 0 else (signo := "cero"):
    print("El número es", signo)
 
 
# Ejercicio 4: Calcular el área de un círculo utilizando una función lambda

import math

radio = float(input("Ingrese el radio del círculo: "))
area = (lambda r: math.pi * r ** 2)(radio)
print("El área del círculo es:", area)
 
 