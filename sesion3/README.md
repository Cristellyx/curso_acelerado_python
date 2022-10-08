# Sesion 3

---
Listado de ejercicios

* ejercicio18.py

Descripción:  Autorización por nombre

```python
'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion3/ejercicio18.py
Autor: Cristell Molina Gomez
Action: Autorización por nombre
'''
personas_autorizadas = ["Alberto", "Carmen", "Cristell", "Hugo", "Lorena"]
nombre = input("Dígame su nombre: ")
if nombre in personas_autorizadas:
  print("Está autorizado")
else:
  print("No está autorizado")
```
<br>
<hr>

* ejercicio19.py

Descripción: Palabra alreves

```python
'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion3/ejercicio19.py
Autor: Cristell Molina Gomez
Action: Palabra alreves
'''
word = input("Introduce una palabra: ")
reversed_word = word
word = list(word)
reversed_word = list(reversed_word)
reversed_word.reverse()
if word == reversed_word:
  print("Es un palíndromo")  
else:
  print("No es un palíndromo")
```
<br>
<hr>

* ejercicio20.py

Descripción: Suma de precios y orden 

```python
'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion3/ejercicio20.py
Autor: Cristell Molina Gomez
Action: Suma de precios y orden
'''
total = 0
prices = [50, 75, 46, 22, 80, 65, 8]
min = max = prices[0]

for price in prices:
  total = total+price
  if price < min:
    min = price
  elif price > max:
    max = price

print("La suma total es "+ str(total))
print("El mínimo es " + str(min))
print("El máximo es " + str(max))
```
<br>
<hr>

* ejercicio21.py

Descripción: Mostrar asignaturas

```python
'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion3/ejercicio21.py
Autor: Cristell Molina Gomez
Action: Mostrar asignaturas
'''

asignaturas = ["Programacion" , "Matematicas", "Fisica", "Historia", "Quimica"]

for f in asignaturas:
  print(f)

```
<br>
<hr>

* ejercicio22.py

Descripción: Ordenar números de loteria  

```python
'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion3/ejercicio22.py
Autor: Cristell Molina Gomez
Action: Ordenar números de loteria
'''
lista = []
for f in range(5):
  numero = int(input("Introduce un numero ganador: "))
  lista += [numero]


lista.sort()
print("-------------------------------")
print("Los numeros ganadores son ")
for f in lista:
  print(f)
```
<br>
<hr>

* ejercicio23.py

Descripción: Producto escalar de vectores

```python
'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion3/ejercicio23.py
Autor: Cristell Molina Gomez
Action: Producto escalar de vectores
'''

a = (1, 2, 3)
b = (-1, 0, 2)
c = (2, 1, 4)
product = 0
for i in range(len(a)):
  product += a[i]*b[i]*c[i]
print("El producto de los vectores" + str(a) +", "+str(b) + " y " + str(c) + " es " + str
(product))
```
<br>
<hr>

* ejercicio24.py

Descripción: Hacer diccionario vacio

```python
'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion3/ejercicio24.py
Autor: Cristell Molina Gomez
Action: Hacer diccionario vacio
'''
persona = {}
continuar = True
while continuar:
  clave = input('¿Qué dato quieres introducir? ')
  valor = input(clave + ': ')
  persona[clave] = valor
  print(persona)
  continuar = input('¿Quieres añadir más información (Si/No)? ') == "Si"
```
<br>
<hr>

* ejercicio25.py

Descripción: Diccionario traductor

```python
'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion3/ejercicio25.py
Autor: Cristell Molina Gomez
Action: Diccionario traductor
'''
diccionario = {}
palabras = input("Introduce la lista de palabras y traducciones en formato palabra:traducción separadas por comas: ")
for i in palabras.split(','):
  clave, valor = i.split(':')
  diccionario[clave] = valor
frase = input('Introduce una frase en español: ')
for i in frase.split():
  if i in diccionario:
    print(diccionario[i], end=' ')
  else:
    print(i, end=' ')
```
<br>
<hr>

* ejercicio26.py

Descripción: Divisas en diccionario

```python
'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion3/ejercicio26.py
Autor: Cristell Molina Gomez
Action: Divisas en diccionario
'''
divisas = {'Euro':'€', 'Dollar':'$', 'Peso':'$'}
ingresar = input('Introduce la divisa que desees conocer: ')
if ingresar in divisas:
  print(divisas[ingresar])
else:
  print("La divisa no esta en el diccionario")
```
<br>
<hr>

* ejercicio27.py

Descripción: Directorio personal

```python
'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion3/ejercicio27.py
Autor: Cristell Molina Gomez
Action: Directorio personal
'''
aux = ["Nombre","Edad","Direccion","Telefono"]
datos = {}

for f in aux:
  valor = input('Introduce el valor '+ f+': ')
  datos[f] = valor

print("---------------------------------")
print(datos["Nombre"]+" tiene "+datos["Edad"]+" años, vive en "+ datos["Direccion"]+" y su numero de telefono es "+ datos["Telefono"])
  

```
<br>
<hr>

* ejercicio28.py

Descripción: Menú facturas

```python
'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion3/ejercicio27.py
Autor: Cristell Molina Gomez
Action: Menú facturas
'''
facturas = {}
cantidad_cobrada ={}
suma = 0
continuar = True
while continuar:
  print("1. Añadir nueva factura")
  print("2. Pagar factura")
  print("3. Salir")
  clave = int(input('Elija un número: '))
  if clave == 1:
    numero_factura = int(input('Introduce el número de factura: '))
    coste = int(input('Introduce el coste: '))
    facturas[numero_factura] = coste
    print("Se ha añadido con exito la factura")
    print(facturas)
    ''' Cantidad pendiente de cobro '''
    for f in facturas:
      suma+= facturas[f]
    print ("*** Cantidad pendiente de cobro: "+str(suma))
    suma = 0
    ''' Cantidad cobrada '''   
    for f in cantidad_cobrada:
      suma+= cantidad_cobrada[f]
    print ("*** Cantidad cobrada: "+str(suma))
    print("---------------------------------------------")
  elif clave == 2:
    num_factura = int(input('Introduce el número de factura a pagar: '))
    if num_factura in facturas:
      cantidad_cobrada[num_factura] = facturas[num_factura]
      facturas.pop(num_factura)
    else:
      print("No se ha encontrado el número ")
    print("Se ha pagado con exito la factura")
    print(facturas)
    ''' Cantidad pendiente de cobro '''
    for f in facturas:
      suma+= facturas[f]
    print ("*** Cantidad pendiente de cobro: "+str(suma))
    suma = 0
    ''' Cantidad cobrada '''   
    for f in cantidad_cobrada:
      suma+= cantidad_cobrada[f]
    print ("*** Cantidad cobrada: "+str(suma))
    print("---------------------------------------------")
  elif clave==3:
    continuar = False
  else:
    print("Elija un numero valido")
print("******** HA SALIDO DE FORMA CORRECTA ********")
```
<br>
<hr>

