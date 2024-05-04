# OPERADORES MORSA
Los operadores de morsa, también conocidos como walrus operators en inglés, **es una característica introducida en Python 3.8 que permite asignar valores a variables como parte de una expresión.** Esto es útil en situaciones donde se necesita evaluar una expresión y al mismo tiempo asignar un valor a una variable.

 **En Python, el operador de morsa (también conocido como operador de asignación condicional) es una característica introducida en la versión 3.8 que nos permite asignar un valor a una variable en función de una condición. Aquí tienes un resumen de los operadores de morsa en Python, junto con algunos ejemplos:**
 
**`El operador de morsa se representa con " := " y se utiliza de la siguiente manera:`**
 
## 1. Asignación condicional:

**- Podemos asignar un valor a una variable basado en una condición utilizando el operador de morsa.**
- Ejemplo:
```PYTHON
edad = 20
estado = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(estado)
 ```
 **En este ejemplo, se asigna el valor "Mayor de edad" a la variable "estado" si la edad es mayor o igual a 18; de lo contrario, se asigna el valor "Menor de edad".**

## 2. Ignorar valores:
 
**- Podemos utilizar el operador de morsa para ignorar valores que no nos interesan al desempaquetar una secuencia.**
- Ejemplo:
```PYTHON
numeros = [1, 2, 3, 4, 5]
_, _, _, cuarto, _ = numeros
print(cuarto)
 ```
 **En este ejemplo, utilizamos el operador de morsa para ignorar los primeros tres valores de la lista "numeros" y asignar el cuarto valor a la variable "cuarto".**
 
**`Recuerda que el operador de morsa solo está disponible a partir de la versión 3.8 de Python. Si estás utilizando una versión anterior, es posible que no puedas utilizar este operador.`**
 
hjgjugjgj
