'''
*********** Curso de programación acelerada en Python ************
Date 07-10-2022
File: sesion3/ejercicio27.py
Autor: Cristell Molina Gomez
Action: Facturas
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

  

