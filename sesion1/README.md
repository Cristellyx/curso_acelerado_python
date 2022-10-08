# Sesion 1

---
Listado de ejercicios

* ejercicio1.py

Descripción: Asignación de variables

```python
'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion/ejercicio1.py
Autor: Cristell Molina Gomez
Action: Asignación de variables
'''
nombre_estado = 'Tabasco'
superficie = 25267
poblacion_total = 2403000000
promedio_temperatura = 31.3
estados_cercanos = ['chiapas','campeche','veracruz']
productos = ['cacao','coco','piña']

print(nombre_estado, " es un estado que ", )
print("con ",estados_cercanos[0], "colinda al sur", "y")
print("Tiene una superficie de ", superficie)
print("Su poblacion total es ", poblacion_total)
print("Su temperatura promedio es de ", promedio_temperatura, "°C")
print("Produce los productos",productos[0])
```
<br>
<hr>

* ejercicio2.py

Descripción: Superficie de un cuadrado

```python
'''
*********** Curso de programación acelerada en Python ************
Date  07-10-2022
File: sesion/ejercicio2.py
Autor: Cristell Molina Gomez
Action: Superficie de un cuadrado
'''
lado=input("Ingrese la medida del lado del cuadrado:")
lado=float(lado)
superficie=lado*lado
print("La superficie del cuadrado es")
print(superficie)
```

<br>
<hr>

* ejercicio3.py

Descripción: Pago de trabajador

```python
'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion/ejercicio3.py
Autor: Cristell Molina Gomez
Action:Pago de trabajador
'''
horas = float(input("Introduce tus horas de trabajo: "))
coste = float(input("Introduce lo que cobras por hora: "))
extra = float(input("Introduce tus horas extra: "))
pago_extra = float(input("Introduce lo que cobras por hora extra: "))
paga = (horas * coste) + (extra * pago_extra)
print("Tu paga es", paga)
```

<br>
<hr>

* ejercicio4.py

Descripción: Índice de masa corporal peso en kg/ estatura mtrs cuadrados

```python
'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion/ejercicio4.py
Autor: Cristell Molina Gomez
Action: Índice de masa corporal peso en kg/ estatura mtrs cuadrados
'''
peso = input("¿Cuál es tu peso en kg? ")
estatura = input("¿Cuál es tu estatura en metros?")
imc = round(float(peso)/float(estatura)**2,2)
print("Tu índice de masa corporal es " + str(imc))
```

<br>
<hr>

* ejercicio5.py

Descripción: Convertir grados de Celsius a Farenheit

```python
'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion/ejercicio5.py
Autor: Cristell Molina Gomez
Action: Convertir grados de Celsius a Farenheit

'''
celsius = float(input("Introduzca los grados celsius: "))
farenheit = celsius * 1.8 + 32
print(str(celsius) + "°C equivale a " + str(farenheit) +"°F")
```

<br>
<hr>

* ejercicio6.py

Descripción: Imprime capital obtenido de una inversión

```python
'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion/ejercicio6.py
Autor: Cristell Molina Gomez
Action: Imprime capital obtenido de una inversión
'''
cantidad = float(input("¿Cantidad a invertir? "))
interes = float(input("¿Interés porcentual anual? "))
años = int(input("¿Años?"))
print("Capital final: " + str(round(cantidad * (interes / 100 + 1) ** años, 2)))
```

<br>
<hr>

* ejercicio7.py

Descripción: Suma de los primeros numeros enteros

```python
'''
*********** Curso de programación acelerada en Python ************
Date: 07-10-2022
File: sesion/ejercicio7.py
Autor: Cristell Molina Gomez
Action: Suma de los primeros numeros enteros
'''
n = int(input("Introduce un número entero: "))
suma = n * (n + 1) / 2
print("La suma de los primeros números enteros desde 1 hasta " + str(n) + " es " + str(suma))
```















